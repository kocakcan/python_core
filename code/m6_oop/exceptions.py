# Exceptions are events occurring during program execution that disrupt the
# normal flow of instructions.

# 1. NameError: Occurs when a variable or name is not found
def name_error_example():
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError occurred: {e}")


# 2. ValueError: Occurs when an operation/function receives an argument with
#    right type but with inappropriate value
def value_error_example():
    try:
        number = int("hello")
    except ValueError as e:
        print(f"ValueError occurred: {e}")


# 3. TypeError - Occurs when an operation/function is applied to an object of
#    inappropriate type
def type_error_example():
    try:
        result = "2" + 2
    except TypeError as e:
        print(f"TypeError occurred: {e}")


# 4. SyntaxError - Occurs when the parser encounters invalid syntax. This can't
#    be caught with try-except as it occurs during parsing
# def syntax_error_example():
#     if True print("Hello")  # missing ':'


# 5. OSError - Occurs when a system operation causes a system-related error
def os_error_example():
    try:
        file = open("nonexistent_file.txt")
    except OSError as e:
        print(f"OSError occurred: {e}")


# 6. RuntimeError - Occurs when an error doesn't fall into any other category
def runtime_error_example():
    try:
        raise RuntimeError("This is a runtime error")
    except RuntimeError as e:
        print(f"RuntimeError occurred: {e}")


# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError("You're kidding")
    return age


# Handling exceptions
def handle_age_validation():
    try:
        age = validate_age(-5)
    except ValueError as e:
        print(f"Invalid age: {e}")
    else:
        print(f"Age is valid: {age}")
    finally:
        print("Age validation completed")


# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  ├── GeneratorExit
#  └── Exception
#       ├── StopIteration
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       ├── SyntaxError
#       │    └── IndentationError
#       ├── SystemError
#       ├── TypeError
#       └── ValueError


def main():
    # name_error_example()
    # value_error_example()
    # type_error_example()
    # syntax_error_example()
    # os_error_example()
    # runtime_error_example()
    handle_age_validation()


if __name__ == "__main__":
    main()
