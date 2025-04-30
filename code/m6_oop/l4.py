# L4: Magic Methods

"""
In Python, there is a function called dir(), which lists all the attributes of
the given object, and if you use dir() function for your object or object
class, you will discover attributes like __class__, __doc__, __str__ etc. These
are called magic methods because they are implicitly called when some action
happens.

Magic methods in Python are the special methods that start and end with double
underscores. Magic methods are not meant to be invoked directly by you, but the
invocation happens internally from the class after a certain action.
"""

"""
Callable Objects

As you know, everything in Python is an object, including functions. In
general, any object can be callable, like functions are. You have to only
define the __call__ magic method in this object. This means that you can write
you own callable objects.
"""


class Callable:
    def __call__(self, *args, **kwargs):
        print("__call__ method is called")


obj = Callable()
obj()

"""
Here, you create a simple Callable class with the __call__() magic method.
Inside this method, you are printing a message.

When you instantiate an object and call that object, a message will be printed.
"""

"""
Iterator Pattern

Iterable is an object with __iter__() magic method. It can be iterated over. An
example of an iterable is a list or tuple. The iterator is the object which
iterates over the sequence (or some non-sequence object like dict or file
objects) in the correct order. It is returned by an __iter__() method of the
itreable object. In addition, iterators have the __next__() method, which
returns the next item of the object.

Iterator also has the __iter__() method that returns self. Note that this
method contradicts the classic iterator pattern.
"""
numbers = [2, 5, 8]
iterator1 = iter(numbers)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
# print(next(iterator1))
