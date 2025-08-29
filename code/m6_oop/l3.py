# L3: Exceptions

"""
Syntax and Logical Errors

You can make mistakes while writing a program that leads to a Python program
terminating as soon as it encounters an unhandled error. These errors can be
broadly classified into two classes:

Syntax errors occur when the programmer doesn't follow the proper
structure/syntax of the language.
Logical errors or exceptions are events raised when the Python encounters
errors while executing the code. They stop the execution and raise exception
objects.
"""

"""
A syntax error occurs when the interpreter translates source code into byte
code. It provides the error's actual description and traces it back and points
to the actual line where the error is corrected.
"""
# print "demonstrate syntax errors"

"""
An exception object describes an exception and traces it back to where the
problem occurred.
For example, if you are trying to read a file that does not exist, it disrupts
the flow of the program and raises a FileNotFoundError
"""
# open("file.txt", "rb")

"""
Handling Exceptions

Exception handling ensures the program doesn't break when the unhandled error
occurs. In Python, exceptions can be handled using a try/except statement.

try:
    # The operation which can cause an exception is placed inside the try
    # clause
    <statements>    # Run this as a normal part of the program
except:
    # The code that handles the exception is written in the except clause.
    # You can choose what operations to perform once you have caught the
    # exception.
    <statements>    # Execute this when there is an exception
else:
    # In the else statement, you can only instruct a program to execute a
    # specific code block if there are no exceptions.
    <statements>    # Execute this only if no exceptions are raised
finally:
    # You can use finally to make sure files or resources are closed or
    # released regardless of whether an exception occurs, if you don't catch
    # the exception.
    <statements>    # Always execute this
"""

# try:
#     fh = open("testfile", "w")
#     fh.write("This is a test")
# except IOError:
#     print("Error: can't find file or read data")
# else:
#     print("File is edited successfully!")
#     fh.close()
# f = open("myfile.txt")
#
# try:
#     print(f.read())
# except:
#     print("Something went wrong")
# finally:
#     f.close()

"""
Handling Specific Exceptions

Built-in or custom exceptions are raised for specific errors and can be
specified in multiple except clauses to distinguish the specific exception.

Follow good programming practice instead of handling every case in the same
way. For example, you can specify which exceptions an except clause should
catch.
"""
# try:
#     # do something
#     pass
# except ValueError:
#     # handle ValueError exception
#     # pass
# except (TypeError, ZeroDivisionError):
#     # handle multiple exceptions
#     # TypeError and ZeroDivisionError
#     pass
# except:
#     # handle all exceptions
#     # pass

"""
Raising Exceptions

The raise statement forces a specified exception to occur. In addition, you can
optionally pass arguments to the exception to clarify why that exception was
raised.
"""

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

"""
User-Defined Exceptions

Python has various built-in exceptions that force your program to raise an
error when something goes wrong.
However, sometimes you may need to create custom exceptions that serve your
needs. Users can defined custom exceptions by creating a new class from the
built-in Exception class. Most of the built-in exceptions are also derived from
the Base Exception class.
You have created a user-defined exception called InputError, inheriting from
the Exception class. Like other exceptions, this new exception class can be
raised using the raise statement with an optional error message.
"""


class InputError(Exception):
    pass


# raise InputError("Custom exception")
"""
Pitfall with Exceptions

Suppose you have Exception1 and Exception2. Exception2 is a subclass of
Exception1 and you try to catch Exception2 in the following situation.
You will always get the "Exception1 is caught" output when running this code
snippet. It happens because Exception1, the superclass of the exception class
Exception2, has already been caught. Order matters.
"""


class FirstException(Exception):
    pass


class SecondException(FirstException):
    pass


# try:
#     if isinstance("can", str):
#         raise SecondException
# except FirstException:
#     raise FirstException("FirstException is caught")
# except SecondException:
#     raise SecondException("SecondException is caught")

# To solve this place the SecondException before the FirstException
try:
    if isinstance(3.14, float):
        raise SecondException
except SecondException:
    raise SecondException("SecondException is caught")
except FirstException:
    raise FirstException("FirstException is caught")
