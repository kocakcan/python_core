# Python Built-In Functions

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __abs__(self):
        return abs(self.age)

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


if __name__ == "__main__":
    main()
