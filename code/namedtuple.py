"""
    collections.namedtuple(typename, field_names, *, rename=False,
    defaults=None, module=None)

    - Returns a new tuple subclass named typename.
    - The new subclass is used to create tuple-like objects that have fields
      accessible by attribute lookup as well as being indexable and iterable.
    - Instances of the subclass also have a helpful docstring (with typename
      and field_names) and a helpful __repr__() method which lists the tuple
      contents in a name=value format.
    - The field_names are a sequence of strings such as ['x', 'y'].
    - Alternatively, field_names can be a single string with each fieldname
      seperated by whitepsce and/or commas, for example 'x y' or 'x, y'.
    - Any valid Python identifier may be used for a fieldname except for names
      starting with an underscore.
    - Valid identifiers consist of letters, digits, and underscores but do not
      start with a digit or underscore and cannot be a keyword such as class,
      for, return, global, pass, or raise.
    - If rename is true, invalid fieldnames are automatically replaced with
      positional names.
    - For example, ["abc", "def", "ghi", "abc"] is converted to ["abc", "_1",
      "ghi", "_3"], eliminating the keyword def and duplicate fieldname abc.
    - defaults can be None or an iterable of default values. Since fields with
      a default value must come after any fields without a default, the
      defaults are applied to the rightmost parameters.
    - For example, if the fieldnames are ['x', 'y', 'z'] and the defaults are
      (1, 2), then x will be a required argument, y will default to 1, and z
      will default to 2.
    - If module is defined, the __module__ attribute of the named tuple is set
      to that value.
    - Named tuple instances do not have per-instance dictionaries, so they are
      lightweight and require no more memory than regular tuples.
"""
from collections import namedtuple
def main():
    Point = namedtuple("Point", ['x', 'y'])
    p = Point(11, y=22) # instantiate with positional or keyword arguments
    print(p[0] + p[1])  # indexable like the plaing tuple (11, 22)
    x, y = p            # unpack like a regular tuple
    print(x, y)

    print(p.x + p.y)    # fields also accessible by name

    print(p)            # readable __repr__ with a name=value style

    # In addition to the methods inherited from tuples, named tuples support
    # three additional methods and two attributes. To prevent conflict with
    # field names, the method and attribute names start with an underscore.
    
    """
        classmethod somenamedtuple._make(iterable)
        Class method that makes a new instance from an existing sequence or
        iterable.
    """
    t = [11, 22]
    print(Point._make(t))

    """
        somenamedtuple._asdict()
        Return a new dict which maps field names to their corresponding values.
    """
    p = Point(x=11, y=22)
    print(p._asdict())

    """
        somenamedtuple._replace(**kwargs)
        Return a new instance of the named tuple replacing specified fields
        with new values.
    """
    p = Point(x=11, y=22)
    print(p._replace(x=33))

    """
        somenamedtuple._fields
        Tuple of strings listing the field names. Useful for introspection and
        for creating new named tuple types from existing named tuples.
    """
    print(p._fields)

    Color = namedtuple("Color", "red green blue")
    Pixel = namedtuple("Pixel", Point._fields + Color._fields)
    print(Pixel(11, 22, 128, 255, 0))

    """
        somenamedtuple._field_defaults
        Dictionary mapping field names to default values.
    """
    Account = namedtuple("Account", ["type", "balance"], defaults=[0])
    print(Account._field_defaults)
    print(Account("premium"))

    # To retrieve a field whose name is stored in a string, use the getattr()
    # function:
    print(getattr(p, 'x'))

    # To convert a dictionary to a named tuple, use the double-star-operator
    d = {'x': 11, 'y': 22}
    print(Point(**d))

    # Since a named tuple is a regular Python class, it is easy to add or
    # change functionality with a subclass.
    class Point(namedtuple("Point", ['x', 'y'])):
        __slots__ = ()
        @property
        def hypot(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        def __str__(self):
            return "Point: x=%6.3f, y=%6.3f, hypot=%6.3f" % (self.x, self.y,
                                                             self.hypot)

    for p in Point(3, 4), Point(14, 5 / 7):
        print(p)

    # The subclass shown above sets __slots__ to an empty tuple. This helps
    # keep memory requirements low by preventing the creation of instance
    # dictionaries.
    
    # Subclassing is not useful for adding new, stored fields. Instead, simply
    # create a new named tuple type from the _fields attribute.
    Point3D = namedtuple("Point3D", Point._fields + ('z',))

    # Docstrings can be customized by making direct assignments to the __doc__
    # fields:
    Book = namedtuple("Book", ["id", "title", "authors"])
    Book.__doc__ += ": Hardcover book in active collection"
    Book.id.__doc__ = "13-digit ISBN"
    Book.title.__doc__ = "Title of first printing"
    Book.authors.__doc__ = "List of authors sorted by last name"
if __name__ == "__main__":
    main()
