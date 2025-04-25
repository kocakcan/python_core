# L3: Import Pitfalls

"""
Import Process

It is worth noting that Python runs all codes when it reaches the import
statement.

In general, the following statements are equal:
from module import func = import module
                          func = module.func
                          del module

Any imported variable can be changed in the module. So it is impossible to
guarantee you have the latest function state until you run all the modules.
"""

"""
Variable PYTHONPATH

For example, you want to import abc module. When Python sees an import abc
statement, it searches abc.py in the working directory. If it does not find it,
Python will throw ModuleNotFoundError.

A list of folders is specified in the PYTHONPATH environment variable.
Sometimes you might see .pyc files. These files are compiled bytecodes of
Python scripts. When you want to run a script, Python first translates a source
code to byte code. However, if it is converted already, this process is
skipped. It will help speed up the execution.

PYTHONPATH is an environment variable you can set to add additional directories
where Python will look for modules and packages.

An installation-dependent list of directories configured at the time Python is
installed. The search path can be accessed through Python variable sys.path,
which is obtained from a module sys.
"""
import sys

print(sys.path)

"""
Variable __name__

Python runs all the code before importing it. If you have print statements and
import the module, they will be printed, but this may not be the desired
result.

The solution is a magic variable __name__. Python sets the __name__ variable to
module name when importing a module. But, when executing this module, __name__
is equal to __main__. Using this fact, you can distinguish between them.
"""

"""
Importing Modules With the Same Functions

There are some problems when you use from the module * statement. The reason is
you have to avoid implicitly loading all of the Python module's locals into and
over our current module's namespace. This can produce unpredictable results.

It is bad practice to use from module import * style of importing. A better
approach is to import the module if you have two functions with the same name
and import, but only the functions and classes needed.
"""

"""
Cyclic Imports

Suppose you have the following two files: a.py and b.py. Each file tries to
import functions from one another.

If you run b.py, you will get the error ImportError: cannot import name 'func2'
from partially initialized module 'a' (most likely due to circular import).
What happens is that when Python sees a statement from a import func2, it tries
to import func2 from a.py, However, in a.py, there is also statement from b
import func1, which creates a cyclic loop.

You can import the module and use the module .func notation to solve this
problem. Another possible solution is to put imports inside functions so that
imports will occur whenever functions are called.
"""

"""
    Execution of __init__ Files When Importing a Package

    The __init__.py file is used to mark directories where it is located as
    Python packages. Let's suppose you have the following structure:

    /folder
    |-> __init__.py
    |-> x.py
    ->y.py
    
    If you want to import x.py, you can type import folder.x or from folder
    import x. However, if you remove __init__.py and try to import it, you will
    get an error.
    
    One interesting thing about __init__.py is that all the code written in it
    will be executed during the import.

    # folder/__init__.py
    # print("inside __init__.py")
    
    # y.py
    # from folder import x
    
    If you run y.py, you will see the printed message inside of __init__.py. It
    can be advantageous when you need to run some piece of code when something
    is imported. For example, one can put tests in __init__.py so that tests
    will be executed wheneve functions or classes are imported.
"""

"""
isort Module

isort arranges your imports for comfortable read. To install this package,
write it in the command line:

pip install isort
isort .
isort main.py
"""

"""
Changing Names

Everything in Python is an object, and you use names to reach these objects.
So, you can change these names:
"""
import datetime

my_time_method = datetime.time
print(my_time_method())
