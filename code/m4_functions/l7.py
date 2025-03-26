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


def main():
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


if "__name__" == "__main__":
    main()
