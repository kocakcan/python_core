# L8: Closure

"""
- The closure is a technique for implementing lexically scoped name binding.
- Operationally, a closure is a record storing a function together with an
  environment.
- The environment is a mapping associating each free variable of the
  function (variables that are used locally, but defined in an enclosing
  scope) with the value or reference to which the name was bound when the
  closure was created.
- Unlike a plain function, a closure allows the function to access those
  captured values or references, even when the function is invoked outside
  their scope.
"""


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function("Hi!")
my_function()

# As you can see, you did not call the inner_function inside the
# outer_function. Instead, you just returned a reference to the inner_function.

# Closures can be helpful when you need to create a pattern for some function
# and then call it.


def format_message(format_string):
    frmt_string = format_string

    def inner_function(message):
        print(frmt_string.format(message))

    return inner_function


my_formatter = format_message("my formatted message: {}")
my_formatter("Hello!")
my_formatter("My name is Tom")


# With closure, you also can implement a counter for function calls.
def function_with_counter():
    count = 0

    def some_function(msg):
        nonlocal count
        count += 1
        print(f"{count:4}: {msg}")

    return some_function


print_with_counter = function_with_counter()
print_with_counter("Hello")
print_with_counter("I count my calls")
