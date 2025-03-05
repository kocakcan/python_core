# Python Built-In Functions

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __abs__(self):
        return abs(self.age)

    @classmethod
    def do_sth(cls):
        print("Engineers are doing something right now!")


def is_even(x):
    return x % 2 == 0

def add_five(x):
    return x + 5

def main():
    """
    abs(x)
        - Return the absolute value of a number.
        - The argument may be an integer, a floating-point number, or an object
        implementing __abs__().
        - If the arugment is a complex number, its magnitude is returned.
    """
    print(f"Absolute value of -5 is: {abs(-5)}")
    print(f"Absolute value of -5.41 is: {abs(-5.41)}")
    print(f"Absolute value of -5.41 is: {abs(-5.41)}")
    print(f"Absolute value of -3+4j is: {abs(-3+4j)}")

    can = People("Can", -27)

    print(f"Absolute value of my age is -> {can.__abs__()}")

    """
    aiter(async_iterable)

    - Return an asynchronous iterator for an asynchronous iterable.
    - Equivalent to calling x.__aiter__()

    Note: Unlike iter(), aiter() has no 2-argument variant.
    """

    """
    all(iterable)

    - Return True if all elements of the iterable are true (or if the iterable
      is empty). Equivalent to:
      
        def all(iterable):
            for element in iterable:
                if not element:
                    return False
            return True
    """

    inputs = [5, "Can", True, [1, 2, 3], {1, 2, 3, 4, 5}, {"name": "Can",
                                                           "age":
                                                           27}]

    print(any(inputs))

    """
    awaitable anext(aysnc_iterator)
    awaitable_anext(aysnc_iterator, default)

    - When awaited, return the next item from the given asynchronous
      iterator, or default if given and the iterator is exhausted.
    - This is the async variant of the next() builtin, and behaves
      similarly.
    - This calls the __anext__() method of async_iterator, returning an
      awaitable. Awaiting this returns the next value of the iterator. If
      default is given, it is returned if the iterator is exhausted,
      otherwise StopAsyncIteration is raised.
    """

    """
    any(iterable)

    - Return True if any element of the iterable is true. If the iterable is
      empty, return False. Equivalent to:

        def any(iterable):
            for element in iterable:
                if element:
                    return True:
            
            return False
    """

    outputs = [
        15,
        3.14,
        0,
        False,
        {},
        [],
        (1,),
    ]

    print(any(outputs))

    """
    ascii(object)

    - As repr(), return a string containing a printable representation of an
      object, but escape non-ASCII characters in the string returned by repr
      using escapes.
    """
    print(ascii("Hello world 🤗"))

    """
    bin(x)

    - Not the League player 😂
    - Convert an integer number to binary string prefixed by "0b".
    - The result is valid Python expression. If x is not a Python int object,
      it has to define an __index__() method that returns an integer.
    """

    print(bin(27))
    print(bin(-10))
    # Without binary prefix, with it
    print((format(14, 'b'), format(14, '#b')))

    """
    class bool(object=False, /)

    - Return a Boolean value, i.e. one of True or False.
    - The argument is converted using the standard truth testing procedure:

        -> constants defined to be False: None and False
        -> zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        -> empty sequences and collections: "", (), [], {}, set(), range(0)

    - If the argument is False or omitted, this returns False; otherwise it
      returns True.
    - The bool class is a subclass of int
    """

    print(bool([]))
    print(bool(set()))

    """
    breakpoint(*args, **kws)

    - This function drops you into the debugger at the call site. Specifically,
      it calls sys.breakpointhook(), passing args and kws straight through.
    - By default, sys.breakpointhook() calls pdb.set_trace() expecting no
      arguments. In this case, it is purely a convenience function so you don't
      have to explicitly import pdb or type as much code to enter the debugger.
    - However, sys.breakpointhook() can be set to some other function and
      breakpoint() will automatically call that, allowing you to drop into the
      debugger of choice.
    - If sys.breakpointhook() is not accessible, this function will raise
      RuntimeError.
    """

    """
    class bytearray(source='b')
    class bytearray(source, encoding)
    class bytearray(source, encoding, errors)

    - Return a new array of bytes.
    - The bytearray class is a mutable sequence of integers in the range 0 <= x
      <= 256. It has the most of the usual methods of mutable sequences, as
      well as most methods that the bytes type has.
    - If it is a string, you must also give the encoding (and optionally,
      errors) parameters; bytearray() then converts the string to bytes using
      str.encode()
    - If it is an integer, the array will have that size and will be
      initialized with null bytes.
    - If it is an object conforming to the buffer interface, a read-only buffer
      of the object will be used as the initial contents of the array.
    - Without an argument, an array of size 0 is created.
    """

    arr = bytearray(5)

    for _ in arr:
        print(_)

    """
    class bytes(source=b'')
    class bytes(source, encoding)
    class bytes(source, encoding, errors)

    - Return a new "bytes" object which is an immutable sequence of integers in
      the range 0 <= x <= 256.
    - bytes is an immutable version of bytearry - it has the same non-mutating
      methods and the same indexing and slicing behaviour.
    - Accordingly, constructor arguments are interpreted as for bytearray().
    - Bytes objects can also be created with literals.
    """

    four_bytes = bytes(4)

    for _ in four_bytes:
        print(_)

    """
    callable(object)

    - Return True if the object argument appears callable, False if not.
    - If this returns True, it is still possible that a call fails, but if it
      is False, calling object will never succeed.
    - Note that classes are callable (calling a class returns a new instance);
      instances are callable if their class has a __call__() method.
    """

    print("Is print() callable?", callable(print))

    """
    chr(i)

    - Return the string representing a character whose Unicode code point is
      integer i.
    - For example, chr(97) returns the string 'a'. This is the inverse of
      ord().
    """
    if chr(65) == 'A':
        print("It's true")

    """
    @classmethod

    - Transform a method into a class method.
    - A class method receives the class as an implicit first argument, just
      like an instance method receives the instance.
    - To declare a class method, use this idiom:

      class C:
      @classmethod
      def f(cls, arg1, arg2): ...

    - The @classmethod form is a function decorator.
    - A class method can be called either on the class (such as C.f()) or on an
      instance (such as C().f()). The instance is ignored except for its class.
      If a class method is called for a derived class, the derived class object
      is passed as the implied first argument.
    - Class methods are different than C++ and Java static methods. If it's
      what you're looking for, then use @staticmethod.
    """

    # class method example
    People.do_sth()

    """
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

    - Compile the source into a code or AST object.
    - Code objects can be executed by exec() or eval().
    - source can either be a normal string, a byte string, or an AST object.
    """

    """
    class complex(number=0, /)
    class complex(string, /)
    class complex(real=0, imag=0)

    - Convert a single string or number to a complex number, or create a
      complex number from real and imaginary parts.
    """

    print(complex("1+3j"))
    print(complex("-Infinity+NaNj"))

    """
    delattr(object, name)

    - This is a relative of setattr(). The arguments are an object and a
      string. The string must be the name of one of the object's attributes.
    - The function deletes the named attribute, provided the object allows it.
    - For example, delattr(x, "foobar") is equivalent to del x.foobar.
    - Name need not be a Python identifier.
    """
    
    """
    enumerate(iterable, start=0)

    - Return an enumerate object. iterable must be a sequence, an iterator, or
      some other object which supports iteration.
    - The __next__() method of the iterator returned by enumerate() returns a
      tuple containing a count (from start which is default to 0) and the
      values obtained from iterating the iterable.
    - Equivalent to:

      def enumerate(iterable, start=0):
        n = start
        for elem in iterable:
            yield n, item
            n += 1
    """

    seasons = ["Spring", "Summer", "Fall", "Winter"]
    print(list(enumerate(seasons)))

    """
    filter(function, iterable)

    - Construct an iterator from those elements of iterable for which function
      is true. iterable may be either a sequence, a container which supports
      iteration, or an iterator.
    - If function is None, the identity function is assumed, that is, all
      elements of iterable that are false are removed.
    - filter(function, iterable) is equivalent to (item for item in iterable if
      function(item))
    """
    print(list(filter(is_even, range(0, 50))))

    """
    format(value, format_spec="")

    - Convert a value to a "formatted" representation, as controlled by
      format_spec.
    - The interpretation of format_spec will depend on the type of the value
      argument; however, there is a standard formatting syntax that is used by
      most built-in types.
    - The default format_spec is an empty string which usually gives the same
      effect as calling str(value).
    """
    print("My name is {}".format(can.name))

    """
    globals()

    - Return the dictionary implementing the current module namespace.
    - For code with functions, this is set when the function is defined and
      remains the same regardless of where the function is called.
    """

    print(globals())

    """
    hash(object)

    - Return the hash value of the object (if it has one).
    - Hash values are integers. They are used to quickly compare dictionary
      keys during a dictionary lookup.
    - Numeric values that compare equal have the same hash value (even if they
      are of different types, as is the case for 1 and 1.0)
    """
    print(hash(1) == hash(1.0))

    """
    hex(x)

    - Convert an integer number to a lowercase hexadecimal string prefixed with
      "0x". If x is not a Python int object, it has to define __index__()
      method that returns an integer.
    """
    print(hex(255))

    # If you want to convert an integer number to an uppercase or lower
    # hexadecimal string with prefix or not, you can use either of the
    # following ways:

    print("%#x" % 255)
    print("%x" % 255)
    print("%X" % 255)
    print(format(255, "#x"))
    print(format(255, "x"))
    print(format(255, "X"))
    print(f"{255:#x}")
    print(f"{255:x}")
    print(f"{255:X}")

    """
    id(object)

    - Return the "identity" of an object. This is an integer which is
      guaranteed to be unique and constant for this object during its lifetime.
      Two objects with non-overlapping lifetimes may have the same id() value.
    - This is the address of the object in memory.
    """
    x = list(range(0, 15, 3))

    for _ in x:
        print(id(_))

    """
    input()
    input(prompt)

    - If the prompt argument is present, it is written to standard output
      without a trailing whiteline. The function then reads a line from input,
      converts it to a string (stripping a trailing whiteline), and returns
      that.
    - When EOF is read, EOFError is raised.
    """
    # name = input("What's your name? ")
    # print(f"My name is {name} yo yo")
    
    """
    isinstance(object, classinfo)

    - Return True if the object argument is an instance of the classinfo
      argument, or of a (direct, indirect, or virtual) subclass thereof.
    - If object is not an object of given type, the function always returns
      False.
    - If classinfo is a tuple of the type objects (or recursively, other
      such tuples) or a Union Type of multiple types, return True if object is
      an instance of any of the types.
    - If classinfo is not a type or tuple of types and such tuples, a TypeError
      exception is raised. TypeError may not be raised for an invalid type if
      an earlier check succeeds.
    """
    print(isinstance(can, People))

    """
    issubclass(class, classinfo)

    - Return True if a class is a subclass (direct, indirect, or virtual) of
      classinfo. A class is considered a subclass of itself.
    - classinfo may be a tuple of class objects (or recursively, other such
      tuples) or a Union Type, in which case return True if class is a subclass
      of any entry in classinfo. In any other case, a TypeError exception is
      raised.
    """

    print(issubclass(People, object))

    """
    iter(object)
    iter(object, sentinel)

    - Return an iterator object.
    - The first argument is interpreted very differently depending on the
      presence of the second argument. Without a second argument, object must
      be a collection object which supports the iterable protocol (the
      __iter__() method), or it must support the sequence protocol (__getitem__()
      method with integer arguments starting at 0).
    - If it does not support either of those protocols, TypeError is raised. If
      the second argument, sentinel, is given, then object must be a callable
      object. The iterator created in this case will call object with no
      arguments for each call to its __next__() method; if the value returned
      is equal to sentinel, StopIteration will be raised, otherwise the value
      will be returned.
    """

    items = ["Mea Culpa", "Prayer", "Rosary Beads", "Collectibles"]
    my_iterator = iter(items)

    print(next(my_iterator))

    """
    len(object)

    - Return the length (the number of items) of an object.
    - The argument may be a sequence (such as a string, bytes, tuple, list, or
      range) or a collection (such as dictionary, set, or frozenset).
    """
    print(len(items))

    """
    map(function, iterable, *iterables)

    - Return an iterator that applies function to every item of iterable,
      yielding the results.
    - If additional iterables arguments are passed, function must take that
      many arguments and is applied to the items from all iterables in
      parallel.
    - With multiple iterables, the iterator stops when the shortest iterable is
      exhausted.
    """
    even_numbers = list(range(0, 50, 2))
    print(even_numbers)
    print(list(map(add_five, even_numbers)))

    """
    max(iterable, *, key=None)
    max(iterable, *, default, key=None)
    max(arg1, arg2, *args, key=None)

    - Return the largest item in an iterable or the largest of two or more
      arguments.
    - If one positional argument is provided, it should be an iterable.
    - The largest item in the iterable is returned. If two or more positional
      arguments are provided, the largest of the positional arguments is
      returned.
    - There are two optional keyword-only arguments. The key argument specifies
      a one-argument ordering function like that used for list.sort().
    - The default argument specifies an object to return if the provided
      iterable is empty. If the iterable is empty and default is not provided,
      a ValueError is raised.
    - If multiple items are maximal, the function returns the first one
      encountered.
    """
    print(max(even_numbers))

    """
    min(iterable, *, key=None)
    min(iterable, *, default, key=None)
    min(arg1, arg2, *args, key=None)

    - Return the smallest item in an iterable or the smallest of two or more
      arguments.
    - If one positional argument is provided, it should be an iterable. 
      The smallest item in the iterable is returned. 
      If two or more positional arguments are provided, the smallest of the positional arguments is returned.
    - There are two optional keyword-only arguments. 
    - The key argument specifies a one-argument ordering function like that used for list.sort(). 
    - The default argument specifies an object to return if the provided iterable is empty. 
    - If the iterable is empty and default is not provided, a ValueError is raised.
    - If multiple items are minimal, the function returns the first one encountered.
    """
    print(min(even_numbers))

    """
    next(iterator)
    next(iterator, default)

    - Retrieve the next item from the iterator by calling its __next__()
      method.
    - If default is given, it is returned if the iterator is exhausted,
      otherwise StopIteration is raised.
    """
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            print("Iterator has been exhausted")
            break

    """
    class object()

    - This is the ultimate class of all other classes. It has methods that are
      common to all instances of Python classes.
    - When the constructor is called, it returns a new featureless object. The
      constructor does not accept any arguments.
    """

    obj = object()
    print(type(obj))
    print(issubclass(object, object))

    """
    open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd= None, opener=None)

    - Open file and return a corresponding file object. If the file cannot be
      opened, an OSError is raised.
    - file is a path-like object giving the pathname (absolute or relative to
      the current working directory) of the file to be opened or an integer
      file descriptor of the file to be wrapped.
    - mode is an optional string that specifies the mode in which the file is
      opened. It defaults to 'r' which means open for reading in text mode.
      Other common values are 'w' for writing (truncating the file it already
      exists), 'x' for exclusive creation, and 'a' for appending.
    """

    """
    pow(base, exp, mod=None)

    - Return base to the power exp; if mod is present, return base to the power
      exp, modulo mod (computed more efficiently than pow(base, exp) % mod).
    - The two-argument from pow(base, exp) is equivalent to using power
      operator base**exp.
    """
    print(pow(14, 2))

    """
    print(*objects, sep=' ', end='\n', file=None, flush=False)

    - Print objects to the text stream file, seperated by sep and followed by
      end.
    - sep, end, file, and flush, if present, must be given as keyword
      arguments.
    - All non-keyword arguments are converted to strings like str() does and
      written to the stream, seperated by sep and followed by end.
    - Both sep and end must be strings; they can also be None, which means
      using the default values.
    - If no objects are given, print() will just write end.
    - The file argument must be an object with a write(string) method; if it is
      not present or None, sys.stdout will be used. Since printed arguments are
      converted to text strings, print() cannot be used with binary file
      objects. For these use file.write(...) instead.
    """

    """
    class property(fget=None, fset=None, fdel=None, doc=None)

    - Return a property attribute.
    - fget is a function for getting an attribute value.
    - fset is a function for setting an attribute value.
    - fdel is a function for deleting an attribute value.
    - And doc creates a docstring for the attribute.
    """

    class C:
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x

        x = property(getx, setx, delx, "I'm the property!")

    c = C()
    c.x = 19
    print(c.x)

    """
    - If c is an instance of C, c.x will invoke the getter, c.x = value will
      invoke the setter, and del c.x the deleter.
    - If give, doc will be the docstring of the property attribute. Otherwise,
      the property will copy fget's docstring (if it exists).
    - This makes it possible to create read-only properties easily using
      property() as decorator
    """

    class Parrot:
        def __init__(self):
            self._voltage = 100000

        @property
        def voltage(self):
            """Get current voltage."""
            return self._voltage

    """
    - The property decorator turns the voltage() method into a "getter" for a
      read-only attribute with the same name, and it sets the docstring for
      voltage to "Get the current voltage."
    - A property object has getter, setter, and deleter methods usable as
      decorators that create a copy of the property with the corresponding
      accessor function set to the decorated function.
    """

    class C:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

    """
    - This code is exactly equivalent to the first example.
    - The returned property object also has attributes fget, fset, and fdel
      corresponding to the constructor arguments.
    """

    """
    __name__

    - Attribute holding the name of the property. The name of the property can
      be changed at runtime.
    """

if __name__ == "__main__":
    main()
