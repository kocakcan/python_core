# L7: Namespaces vs Scopes

"""
- A namespace is a dictionary for mapping symbolic names to their values.
- When you do any assignment, you are, in fact, updating a namespace
  dictionary.
- When you refer to an object by its name, Python looks through a list of
  several namespaces trying to find one with the name as a key.

- A scope, in comparison, defines which namespaces will be looked in and in
  what order.
- The scope of any reference always starts in the local namespace and moves
  outwards until it reaches the module's global namespace before moving on
  to the built-ins, which is the last level of namespaces.
"""

"""
    - The scope is a rule for finding bindings (value with assigned name),
      while namespaces are a dictionary for storing all variables.
    - You can think of namespaces as a way to organize code so that names don't
      clash (if it is similar in classes/modules).
    - While the scope answers the question: "What value will I get when trying
      to resolve some name for this piece of code? How will I get it?".
"""

"""
    Namespace Dictionaries

    - Namespaces are dictionaries where keys are object names and values are
      the objects.
    - Built-in Namespace: Concerning the built-in namespace, it does not behave
      like a dictionary. Python implements it as a module.
    - Global and Local Namespaces: On the other hand, these are really
      dictionaries for global and local namespaces. Python does implement these
      namespaces as dictionaries.

    - The Python interpreter provides two built-in functions: globals() and
      locals() that allow you to access global and local namespace
      dictionaries.
    - The globals() function returns the dictionary implementing the current
      module namespace. You can even use it to access the objects in the global
      namespace.
"""


def sum_numbers(x, y):
    res = x + y
    print(locals())
    return res


def say_hello():
    name = "John"
    print(f"Hi {name}")


print(globals())

# As you can see, globals() already has several entries. The list of
# globals() may vary slightly, depending on the operating system and
# version of Python.

# Now, let's define a variable
a = "bar"
print(globals())

# Our variable "a" appears in the global namespace. In addition to the
# usual way of accessing an object by its symbolic name "a", you can also
# access it "indirectly" through the global namespace dictionary.
print(globals()["a"])

# Even more, you can edit variable values through the globals() function.
globals()["a"] = 3.14
print(globals()["a"])

print(sum_numbers(3, 8))

# In this case, locals() returns a dictionary with variables for the
# function's sum_numbers local namespace.
# In general, locals() are similar to globals(), but with some differences:
# Call location inside the function: global variables, including a function
# -> globals(), Locally defined variables, Input arguments for a function
# -> locals()
# Call location in a module level: global variables -> globals(), global
# variables -> locals()
# Modification possibility: Yes, returns an actual reference to the global
# namespace dictionary -> globals(); No, returns only a copy of the local
# namespace. Thus, a change of locals() dictionary will not affect a real
# local namespace.


def foo():
    msg = "some message"
    loc = locals()
    print(loc)
    loc["msg"] = "changed message"
    print(msg)


foo()

# Since namespaces are implemented using dictionaries, you can explain why
# you might redefine objects. As you might know, dictionaries in Python are
# implemented with hash tables.

# A hash table is a data structure that stores a collection of key-value
# pairs. Hence, the dicitonary cannot store multiple identical keys.

# What happens if you try to get access and modify a variable outside the
# local scope.

name = "Tom"
say_hello()
print(name)

# When the Python interpreter executes the assignment name = "John", it creates
# a new local reference to a string "John". At that moment, say_hello() loses
# the reference to the object name outside the local scope. So, the local
# assignment doesn't affect the global object.
# The print statement refers to the local variable "name" with the value "John"
# when executing the print statement. But after say_hello() terminates, the
# name again refers to the value in global scope -> "Tom".

# NOTE! Please don't forget that Python has mutable data types. They can be
# modified outside the current scope.
some_list = [4, "foo", 3.14]


def b():
    some_list[1] = "bar"


print(some_list)
b()

# In this case, the variable some_list is defined in the global scope and
# modified in the local scope for the function b()

# In Python, a function can modify an object outside its local scope with one
# the keywords: global, nonlocal.

# x = 10
#
#
# def y():
#     global x
#     x = "foo"
#
#
# print(x)
# y()
# print(x)

# A statement global x means, while executing some function, x refers to the
# object in the global namespace.

# x = 10
#
#
# def y():
#     globals()["x"] = "foo"
#
#
# print(x)
# y()
# print(x)

# You can get the same using the globals() function.
# The statement global x creates a variable 'x' in the global namespace if the
# 'x' is first mentioned inside a function with global x


# def y():
#     global x
#     x = "bar"
#     print(x)
#
#
# y()
# print(x)

# The variable 'x' was created in the global scope during the execution of the
# y() function


# def y():
#     def z():
#         nonlocal x
#         x = "bar"
#         print(x)
#
#     z()
#     print(x)

# Note that the variable 'x' cannot be created in the enclosed space with the
# nonlocal function. Therefore, it will raise an error.

# x = 1
# y = "foo"
#
#
# def test():
#     global x
#     global y
#
#     x = "bar"
#     y = 3.14
#     print(x, y)
#
#
# test()
# print(x, y)

# You can define global names seperately in each line.

# x = 1
# y = "foo"
#
#
# def test():
#     global x, y
#
#     x = "bar"
#     y = 3.14
#     print(x, y)
#
#
# test()
# print(x, y)

x = 10


def y():
    x = "enclosing"

    def z():
        # global x
        nonlocal x
        x = 3.14
        print(f"local {x = }")

    z()
    print(f"enclosing {x = }")


y()
print(x)

# A nonlocal statement works similar to the global, but in the case with nested
# functions.

"""
    Although Python provides global and nonlocal keywords, it's not always
    recommended to use them. If a function modifies data outside of its local
    scope (either by using keywords global or nonlocal or by changing the
    object with the mutable type), this is called a side effect. The situation
    is similar to when a function changes one of its input arguments.

    Therefore, frequent use of changing global variables is generally
    considered unwise. And not only in Python but in other programming
    languages.

    But it's worth mentioning that it's just a matter of style and preference,
    as with many other things. For example, there are cases when modifying
    global variables usage can reduce a program's complexity and make it more
    readable and clear.
"""
