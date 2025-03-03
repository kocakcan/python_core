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


if __name__ == "__main__":
    main()
