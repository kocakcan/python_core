# L6: Namespaces

"""
- Everything in Python is an object: variables, functions, etc.
- An equal sign creates a symbolic name for a created object that you can
  use to reference it. The statement name = "Can" means that you create a
  string object Can and assign it to a symbolic variable name.
- To be able to track all symbolic names so that they don't interfere with
  one another, Python uses namespaces.
- In Python a namespace is the place where a variable is stored. Namespaces
  are implemented as dictionaries, where keys are the object names, and the
  values are the objects themselves.
- In Python, there are four types of namespaces: Built-in, Global,
  Enclosing, and Local.
"""

"""
    Built-In Namespace

    - Namespaces have differing lifetimes. As Python executes a program, it
      creates namespaces as necessary and deletes them when they're no longer
      needed. So typically, many namespaces will exists at any given time.
    - The built-in namespace contains the names of all of Python's built-in
      objects.
    - It is created when you start the Python interpreter and exists as long as
      it runs.
    - Names from this namespace are available at all times when Python is
      running.
    - You can observe objects from the built-in namespace with command
      dir(__builtins__).
    - The Python interpreter creates the built-in namespace when it starts and
      remains in existence until the interpreter terminates. It is why built-in
      functions like id(), print(), etc. are always available from any part of
      the program.
"""

"""
    Global Namespace

    - The global namespaces are created when the main program body starts and
      remains until the interpreter terminates.
    - The global namespace contain names at the level of the main program.
    - The interpreter also creates a global namespace for any module your
      program loads with the import statement.
    - Different namespaces can exists at the same time and be completely
      isolated. Hence, the same name that may exist in different modules
      doesnt' collide.
"""

"""
    Enclosed and Local Namespaces

    - For each function, the interpreter creates a new namespace that is local
      to that function and exists until the function terminates.
    - You can also define one function inside another.
"""


def say_hello(name):
    print('Start "say_hello"')

    def prepare_greeting():
        print('Start "prepare_greeting"')
        greeting = f"Hello, {name}"
        print('End "prepare_greeting"')
        return greeting

    greeting = prepare_greeting() + " from the Python"
    print(greeting)
    print('End "say_hello"')


# In the example above, the function prepare_greeting is defined inside another
# function say_hello.
# When you call say_hello(), Python creates a new namespace for say_hello.
# Similarly, when say_hello calls prepare_greeting, prepare_greeting gets its
# seperate namespace.
# The namespace created for prepare_greeting is the local namespace, and the
# namespace created for say_hello is the enclosing namespace.

# The enclosed namespace includes names defined inside an outer function.
# The local namespace includes local names inside a function.

# Each of these namespaces remains until its corresponding function terminates.
# So, it might take some time before Python can reclaim the memory alotted for
# those namespaces when their functions terminate. But all object references
# they contain stop being valid.

# Built-in functions    -> Built-in namespace
# Imported module       -> Global namespace
# Local function        -> Local namespace

"""
    LEGB Rule

    - So, multiple seperate namepaces can exist during program execution.
      Therefore, you can conclude that several instances of a particular
      symbolic variable name can exist simultaneously in different namespaces
      during the program execution. Because every instance belongs to a
      different namespace, they are all maintained seperately and won't
      interfere with each other.
    - Imagine that you refer to the name a in your code. And the name a exists
      in several namespaces. The concept of scope helps Python to understand
      which one you mean.
    - The scope of the name is the program's scope in which this given
      specified name has a meaning.
    - The interpreter determines it during the runtime based on the name
      definition place and name referencing place in the code. So, in case you
      are referring to the variable a, the interpreter searches for a name a
      from the inside out, looking in the Local, Enclosing, Global, and finally
      in the Built-in scope, also known as LEGB rule.
    - Local Level: If you refer to a inside a function, the interpreter first
      searches for it in the innermost scope. That is local to that function.
    - Enclosing Level: Next, if a was not found in the local scope, the
      interpreter goes to check the outer function (if it exists). The
      interpreter searches in the enclosing funciton's scope.
    - Global Level: The next level is a global namespace. If none of the
      already listed searches have yielded results, then the interpreter looks
      for the following - global context.
    - Built-in Level: If the interpreter cannot find a anywhere else, then they
      will try the built-in scope.
    - In case the interpreter does not find the name, then Python raises a
      NameError exception.
"""
name = "global"


def a():
    name = "enclosing"

    def b():
        name = "local"
        print(name)

    b()


def main():
    # print(dir(__builtins__))

    say_hello("Can")
    a()


if __name__ == "__main__":
    main()
