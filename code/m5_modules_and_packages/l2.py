# L2: Packages

"""
What are Packages or Libraries?

A package in Python is a directory that includes other subpackages and
modules but also contains an __init__.py file. This file helps the Python
interpreter understand that this directory is a package. Packages need to
form a namespace and provide a high level of nesting.

The file __init__.py can be empty but can also restrict which objects will
be available from the package through an __all__ statement.
"""

# file __init__.py
# from module1 import method1
# from module2 import method2, method3
#
# __all__ = ("method1", "method2")

# As a result, method3 won't be available for import from another code that
# uses this method.
