import functools
import time

# A decorator is just a function that takes a function and returns a
# (usually different) function. `@log_call` above a def is sugar for
# `say_hi = log_call(say_hi)`.
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_call
def say_hi(name):
    return f"hi {name}"


say_hi("Can")

# Proof that decoration is just reassignment under the hood.
def add(a, b):
    return a + b


add = log_call(add)
add(2, 3)


# Without functools.wraps, the wrapper shadows the original function's
# identity. That breaks introspection, debuggers, and anything relying on
# __name__/__doc__ (e.g. help(), logging, some framework registries).
def broken_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@broken_decorator
def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}"


print(greet.__name__)  # "wrapper", not "greet" -- identity got lost
print(greet.__doc__)   # None, not "Return a greeting for name."


# functools.wraps copies over __name__, __doc__, __module__, etc. from the
# original function onto the wrapper, so the decorated function still looks
# like itself.
def fixed_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@fixed_decorator
def greet_fixed(name):
    """Return a greeting for name."""
    return f"Hello, {name}"


print(greet_fixed.__name__)  # "greet_fixed"
print(greet_fixed.__doc__)   # "Return a greeting for name."


# Decorator factories: a decorator that itself takes arguments needs an
# extra layer of nesting -- the outer function takes the decorator's own
# arguments and returns the actual decorator.
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(n=3)
def roll_die():
    return "rolled"


print(roll_die())


# Timing decorator: measure wall-clock time around the call using
# perf_counter (monotonic, high-resolution, immune to system clock changes --
# unlike time.time()), and still return the wrapped function's own result.
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


print(slow_sum(10_000_000))
