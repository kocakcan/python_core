from contextlib import contextmanager
import time

# A context manager is just an object implementing __enter__/__exit__.
# `with X() as x:` calls __enter__ before the block and __exit__ after --
# guaranteed, even if the block raises. This is Python's answer to
# "acquire, use, release" without a manual try/finally at every call site.
class Connection:
    def __enter__(self):
        print("opening connection")
        return self  # becomes `x` in `with Connection() as x`

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing connection")


with Connection() as conn:
    print("using connection")

print("---")


# __exit__ always receives the exception info (or all None if no exception).
# Returning a truthy value from __exit__ SUPPRESSES the exception -- it
# never reaches code outside the `with` block. Returning False/None lets it
# propagate normally after cleanup still runs. This is the detail worth
# knowing cold: cleanup and suppression are two separate decisions.
class SuppressingConnection:
    def __enter__(self):
        print("opening connection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing connection")
        if exc_type is ValueError:
            print(f"swallowed a {exc_type.__name__}: {exc_val}")
            return True  # suppress -- the with block ends quietly
        return False  # propagate anything else


with SuppressingConnection():
    print("about to raise ValueError")
    raise ValueError("bad data")

print("reached this line -- the ValueError was suppressed")

try:
    with SuppressingConnection():
        raise RuntimeError("not swallowed")
except RuntimeError as e:
    print(f"caught outside the with block: {e}")

print("---")


# contextlib.contextmanager turns a generator into a context manager without
# writing a class. Code before `yield` is __enter__, the yielded value is
# what `as x` binds to, and code after `yield` is __exit__. The try/finally
# is what guarantees the cleanup half runs even if the block raises --
# without it, an exception in the block would skip cleanup entirely.
@contextmanager
def connection():
    print("opening connection")
    try:
        yield "connection-handle"
    finally:
        print("closing connection")


with connection() as handle:
    print(f"using {handle}")

try:
    with connection() as handle:
        raise ValueError("boom")
except ValueError:
    print("cleanup still ran above, then this exception propagated")

print("---")


# Practical example: timing a block of work. Same idea as the @timer
# decorator, but scoped to an arbitrary chunk of code rather than a whole
# function call -- context managers and decorators both solve setup/teardown,
# just at different granularities (a block vs an entire function).
@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed:.4f}s")


with timed("sum of 10M"):
    total = sum(range(10_000_000))

print(total)
