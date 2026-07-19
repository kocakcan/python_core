# try/except/else/finally, in the order Python actually runs them:
# - try: the code that might fail
# - except: runs only if a matching exception was raised
# - else: runs only if NO exception was raised -- lets you separate "the
#   risky part" from "what to do once it succeeded" instead of cramming
#   both into the try block (where a bug in the success path could get
#   mis-attributed to the try's expected failure).
# - finally: always runs, exception or not, even if the block returns --
#   this is where you put cleanup that must happen no matter what.
def parse(value):
    try:
        result = int(value)
    except ValueError:
        print(f"couldn't parse {value!r}")
        return None
    else:
        print(f"parsed {value!r} -> {result}")
        return result
    finally:
        print(f"done attempting {value!r}")


parse("42")
parse("not a number")

print("---")


# Custom exceptions: subclass Exception (or a more specific builtin) when
# the caller needs to distinguish "this specific failure mode" from generic
# errors -- e.g. to catch it separately, attach structured data, or because
# `except ValidationError` documents intent better than `except ValueError`
# at the call site. Don't bother if a builtin already says exactly what
# went wrong (ValueError, KeyError, TypeError) -- a custom class only earns
# its keep when it adds meaning or extra data.
class ValidationError(Exception):
    def __init__(self, field, value, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"{field}={value!r}: {reason}")


def validate_row(row):
    # Data-pipeline-flavored example: validating one record before it's
    # allowed into a downstream sink. Raising a specific exception type lets
    # a caller decide per-error-type handling (skip the row? quarantine it?
    # abort the whole batch?) instead of pattern-matching a message string.
    if "id" not in row:
        raise ValidationError("id", None, "missing required field")
    if not isinstance(row.get("amount"), (int, float)):
        raise ValidationError("amount", row.get("amount"), "must be numeric")
    return row


rows = [
    {"id": 1, "amount": 10.5},
    {"id": 2, "amount": "oops"},
    {"amount": 5},
]

good, bad = [], []
for row in rows:
    try:
        good.append(validate_row(row))
    except ValidationError as e:
        bad.append(e)
        print(f"quarantined row: field={e.field} reason={e.reason}")

print(f"{len(good)} good rows, {len(bad)} quarantined")

print("---")


# Exception chaining: `raise X from Y` sets __cause__ explicitly, so the
# traceback shows "the above exception was the direct cause of the
# following exception" instead of the vaguer implicit chaining you get for
# free when an except block itself raises ("during handling of the above
# exception, another exception occurred"). Both preserve the original
# traceback -- chaining is about *why* you're re-raising as a different
# type, not about hiding the root cause. `raise X from None` explicitly
# suppresses the chain when the original really is irrelevant noise.
def load_config(raw):
    try:
        return int(raw)
    except ValueError as e:
        # translate a low-level parsing error into a domain-specific one,
        # while keeping the original traceback attached for debugging
        raise ValidationError("config", raw, "not a valid integer") from e


try:
    load_config("abc")
except ValidationError as e:
    print(f"caught: {e}")
    print(f"caused by: {e.__cause__!r}")
