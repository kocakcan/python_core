"""
- Modules and packages refer to modular programming. According to this
  concept, large tasks are broken into smaller manageable subtasks or
  modules. These small pieces can be combined to create complex
  applications. Splitting large applications into smaller parts brins the
  following benefits: Readability, maintainability, reusability,
  manageability.
"""

"""
    What are Modules?

    It is essential to know that the modules as packages can be written not
    only in Python but also in C/C++ language (in the case of using CPython by
    default) or in Java (when using Jython). It depends on the interpreter, as
    to which one you use. These modules are included in the standard library.

    The module is just a program file without executed but callable code.
    Methods are not called inside modules like starting a web server or
    creating a file on the OS file system

    The advantages of storing code in modules are the ability to:

    - reusability of code (DRY principle - Don't Repeat Yourself)
    - easier debugging,
    - readability,
    - easier to avoid collisions between namespaces.
"""

"""
    Imports

    The Python import statement takes the code from one module into another
    program. You can import all the code from a moudle by specifying the import
    keyword followed by the module you want to import. Import statements appear
    at the top of a Python file, beneath any existing comments. In Python,
    there are three ways to import the code from modules.
"""

# You can import the whole module using the "import" statement.
# To do it, you should use the following formula:
# import [module name]

# Let's import the module time from Python's standard library:
import time

# You have imported the time into your code in the above example, so now you
# can access all the time functions in your main program. Suppose you want to use the
# sleep() method in the time module. You can do so using the following code:

# method sleep() is used from Python's standard module time
time.sleep(3)

# Also, you can use multiple imports:
import time
import random

# You can use multiple imports in one line. But this option violates the PEP8
# standard because imports should usually be on seperate lines.
# import time, random # Wrong

# 2. Importing Only Some Methods
# You can import not just the whole module, but only some methods that you
# need. In this case, you should use the from statement:
# from [module name] import [function or value]

# Suppose you only want to import the sleep() function from the time module
# into your code. You can do so in the following way:
from time import sleep

# Try to avoid the symbol * in imports because it can violate the program
# namespace in the same cases.

# from time import *

# Imagine you want to get the time in seconds because the epoch is a
# floating-point number. Python will call method from the last import, and
# because the datetime module also has a time method, that method will be
# called.

from time import time
from datetime import *

print(time())

# 3. Importing With Module Aliases
# You can use imports with module aliases. To do it, you should use the
# following formula:
# from [module name] import [function or value] as [your module alias]
# or
# import [function or value] as [your module alias]

# Sometimes, the names of your methods, classes, or modules can be the same in
# a code. To not violate the program namespace, you can alias your imports:
from time import time as t_time
from datetime import time as dt_time

# Or in this case, you can call these methods by using aliases.
print(t_time())
print(dt_time())

# In addition, there are two types of imports. The first is absolute, when you
# write the full path to the module.
# from my_application.service.module1 import method1

# The second is relative, where the dot means current directory:
# from .module1 import method1
# or
# from . import module1
