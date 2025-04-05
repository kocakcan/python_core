# Nested Decorators
# Decorators can be nested.


# Example Without Decorators Syntax
# def milk(func):
#     def wrapper():
#         print("hot milk")
#         func()
#
#     return wrapper
#
#
# def sugar(func):
#     def wrapper():
#         print("sugar")
#         func()
#
#     return wrapper


# And create a main function (origin function)
# def coffee(variety="arabica"):
#     print(variety)


# If you call the coffee() function, you will see the following:
# coffee()

# But if you will redefine this function, the result will change:
# coffee = sugar(milk(coffee))
# coffee()

# Example With Decorators Syntax
# Using decorators simplify the code. The same example but with decorators
# syntax will look like this


# def milk(func):
#     def wrapper():
#         print("hot milk")
#         func()
#
#     return wrapper
#
#
# def sugar(func):
#     def wrapper():
#         print("sugar")
#         func()
#
#     return wrapper
#
#
# @sugar
# @milk
# def coffee(variety="arabica"):
#     print(variety)
#
#
# coffee()

# The Order of Decoration
# Please, be careful. The order of decoration is important:


def milk(func):
    def wrapper():
        print("hot milk")
        func()

    return wrapper


def sugar(func):
    def wrapper():
        print("sugar")
        func()

    return wrapper


@milk
@sugar
def coffee(variety="arabica"):
    print(variety)


coffee()


# Passing Arguments to the Decorated Function
# Decorators allow you to implement one important functionality, passing
# arguments to the decorated function.
def decorator_for_function_with_arguments(origin_function):
    # Arguments come to the original function from here
    def wrapper(arg1, arg2):
        print("Input arguments:", arg1, arg2)
        origin_function(arg1, arg2)

    return wrapper


@decorator_for_function_with_arguments
def introduce_yourself(first_name, last_name):
    print(f"Hi, my name is {first_name} {last_name}")


introduce_yourself("Peter", "Parker")


# Arguments can also be passed to the decorator itself.
def decorator_maker(decorator_arg1, decorator_arg2):
    print(
        "I create decorators. I got the following arguments:",
        decorator_arg1,
        decorator_arg2,
    )

    def decorator_function(func):
        print("I am a decorator. I got a function:", func)

        def wrapper(function_arg1, function_arg2):
            print(
                "I am a wrapper around the origin function.\n"
                "And I have access to all arguments: \n"
                f"\t- and decorator: {decorator_arg1} {decorator_arg2}\n"
                f"\t- and functions: {function_arg1} {function_arg2}"
            )
            return func(function_arg1, function_arg2)

        return wrapper

    return decorator_function


# The decorator_maker function and decorator_function will be called only once
# when Python creates a decorator with the next statement:
@decorator_maker("Tom", "Jerry")
def origin_function(function_arg1, function_arg2):
    print(f"{function_arg1} {function_arg2}")


# The additional code inside the "wrapper" function will be called every time
# you call a decorated function:
origin_function("Rick", "Morty")


# Saving Values Between Decorated Function Calls
# There is one more interesting case of using decorators, to save values
# between decorated function calls.
def call_counter(origin_function):
    count = 0

    def wrapper(func_arg):
        nonlocal count
        count += 1
        print(f"call number is {count}")

        return origin_function(func_arg)

    return wrapper


@call_counter
def say_hello(guest_name):
    print(f"Hello, {guest_name}")


say_hello("John Doe")
say_hello("Olavi Mikkonen")
