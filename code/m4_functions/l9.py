# L9: Decorators

"""
Design Patterns

- In software engineering, design patterns represent some of the best
  practices adopted by experienced software developers.
- Each pattern is like a blueprint that you can customize to solve a
  particular design problems in your code.
- A software design pattern is a general, reusable solution to a commonly
  occurring problem withing a given context in a software design.
- A design pattern isn't a finished design that can be transformed directly
  into code. It is a description or template for how to solve a problem
  that can be used in many different situations.
"""

"""
    Decorators

    - This pattern is already implemented in Python.
    - Everything in Python is object, including functions, meaning you can
      assign a function object to some variable, return it from another
      function, or provide it as an input argument.
    - Decorators are helpful tools in Python because they allow programmers to
      modify a function's behaviour without modifying a function's code.
    - A decorator is a function that takes in a function as an input argument
      and returns a supplemented copy of that function.
"""


# Within itself, the decorator defines a "wrapper" function. It will be wrapped
# around the original function provided as an argument (being decorated),
# allowing arbitrary code to be executed before and/or after it, as in the
# example below:
def my_decorator(function_to_decorate):
    def wrapper_around_original_function():
        # Put here the code you want to be executed before calling the original
        # function.
        print("I am a code running before the original function.")
        # Then call the original function.
        function_to_decorate()
        # And here will be a code that will run after calling the original
        # function.
        print("I am the code that runs after")

    # At the end, just return a wrapper function that contains the original
    # function and the code that needs to be executed before and after.
    return wrapper_around_original_function


# Now, let's implement a function you do not plan to change anymore.
def stable_function():
    print("I am just a standalone stable function. Nobody must change me!")


stable_function()

# You cannot change the code for stable_function. But you can change its
# behaviour. You just need to decorate it.

# You will pass the stable_function into a decorator, and the decorator will
# wrap the original function in whatever code you need. And finally, return a
# new, ready-to-use function:
decorated_stable_function = my_decorator(stable_function)

# You can redeclare a stable_function, so every time you call it, it runs a
# decorated_stable_function instead.
stable_function()
stable_function = my_decorator(stable_function())
stable_function()


# This is how the previous example could have been written using decorator
# syntax:
# @my_decorator
# def stable_function():
#     print("I am just a standalone stable function. Nobody must change me!")
#
#
# stable_function()

# The decorator is just syntactic sugar for constructs like this
# stable_function = my_decorator(stable_function)

# @my_decorator
# def stable_function():
#     print("I am just a standalone stable function. Nobody must change me!")
#
# def stable_function():
#     print("I am just a standalone stable function. Nobody must change me!")
#
# stable_function = my_decorator(stable_function)

# Decorators are a pythonic implementation of the decorator design pattern.
