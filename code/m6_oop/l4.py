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

# Once the iterator stops working, it should raise the Stop Iteration
# exception.

# Most people love Python because of its clear and beautiful syntax compared to
# other programming languages.
numbers = [2, 5, 7, 1, 0]
for num in numbers:
    print(num)


# Iterator protocol: Objects, which implement __iter__() and __next__() magic
# methods work with for loops.
class Repeat:
    def __init__(self, msg):
        self.msg = msg

    def __iter__(self):
        return self

    def __next__(self):
        return self.msg


# Here you create a simple Repeat class with the msg attribute. You just return
# our object in the __iter__() method. Our __next__() method is returning the
# msg attribute.
# obj = Repeat("car")
# for msg in obj:
#     print(msg)

# obj_iterator = obj.__iter__()
# while True:
#     message = obj_iterator.__next__()
#     print(message)
# If you run the code snippet above, you will get "car" printing continuously;
# to stop it, just press Ctrl + C. You may be wondering: what is happening here
# and how for loops work? Let's convert the for loop above to answer these
# questions. As you can see, the for loop is just a syntactic sugar for a while
# loop. First, you created an iterator object from our obj. Then, in the True
# loop, you called __next__() to retrieve the values and print them.

"""
Finite Iterator

Let's create an iterator object that will be printed a finited number of times
and proceed with it step-by-step again.
"""


class FiniteRepeat:
    def __init__(self, msg, max_count):
        self.msg = msg
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.msg


# Here two more attributes were added: count and max_count, to track
# occurrences. Also, in the __next__() method, you can check whether the count
# is more than max_count; If so, you raise the StopIteration exception. Run the
# following code:
obj = FiniteRepeat("car", 5)
obj_iterator = iter(obj)
# while True:
#     try:
#         message = next(obj_iterator)
#     except StopIteration:
#         break
#     print(message)

# You will notice "car" is printed five times. When the count attribute reaches
# five, the __next__() method raises StopIteration. When for loop receives a
# StopIteration exception, it breaks the loop. You can also convert the for
# loop above to while, and it will work the same way.

"""
Context Managers

Different programming languages have the tools to work with files, databases,
or network connections. Managing these resources correctly is quite tricky. You
must release these resources after usage, not lock them from other programs or
users. The improper usage of these resources can lead to memory leaks because
modern operating systems limit resource use. Cases of exceeding these limits
using files, databases, or network connections can be stopped by the operating
system or any other resource management system.
Python suggests solving resource management problems like these with context
managers. The most well-known and simple context manager is a file object. This
object defines the runtime context to be established when executing a with
statement to open a file:
"""
with open("data.txt") as f:
    data = f.read()


class ContextManager:
    def __init__(self):
        print("__init__ method called")

    def __enter__(self):
        print("__enter__ method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__ method called")


with ContextManager() as manager:
    print("inside with statement block")


# The idea is simple: You need to open a connection to a database or file and
# then close it. You can use the example of an office: first, you need to open
# the door, work inside it, and before leaving the office, you need to close
# it. So let's create a simple context manager.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# The ContextManager object is created and assigned to the manager variables in
# our example. Then methods are executed in the following order: __init__(),
# __enter__(), code inside with block, __exit__(). As you can see, the order is
# critical. Let's now write our version of file resource management. You can
# verify that our context works by checking whether the file is closed:
# print(f.closed)

with FileManager("data.txt", "w") as f:
    f.write("First Line\n")
    f.write("Second Line")

# Connections are not the only way to use context managers. For example, you
# can use them for benchmarking, logging, and other cases.
