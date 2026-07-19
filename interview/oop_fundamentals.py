# Class basics: a class bundles state (instance attributes) with behavior
# (methods). Every instance method's first parameter is the instance itself
# ("self") -- Python passes it implicitly when you call obj.method(), it's
# just a naming convention, not a keyword.
class Animal:
    sound = "..."  # class attribute -- shared by all instances unless overridden

    def __init__(self, name):
        self.name = name  # instance attribute -- unique per object

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    sound = "Woof"  # overrides the class attribute, not the whole class


class Cat(Animal):
    sound = "Meow"


for animal in (Dog("Rex"), Cat("Tom")):
    print(animal.speak())

print("---")


# Inheritance + super(): super().__init__() calls the parent's constructor so
# you extend behavior instead of duplicating it. MRO (method resolution
# order) is the rule Python uses to decide which class's method runs when
# there's more than one candidate (relevant once you have multiple
# inheritance) -- Cls.__mro__ shows the exact lookup order left-to-right.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name}, ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, reports):
        super().__init__(name, salary)  # reuse Employee's init instead of repeating it
        self.reports = reports

    def describe(self):
        base = super().describe()  # reuse the parent's formatting too
        return f"{base}, manages {len(self.reports)} people"


mgr = Manager("Ana", 95000, ["Sam", "Lee"])
print(mgr.describe())
print(Manager.__mro__)

print("---")


# @classmethod vs @staticmethod vs a plain instance method.
# - instance method: needs `self`, operates on one specific object's state.
# - @classmethod: gets `cls` instead of `self` -- doesn't need an instance,
#   but does need the class. Idiomatic for alternate constructors, because
#   `cls(...)` still respects subclassing (calling it on a subclass builds
#   a subclass instance, not hardcoded to the base class).
# - @staticmethod: gets neither. It's just a function namespaced inside the
#   class because it's conceptually related, not because it needs class or
#   instance data.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_tuple(cls, pair):
        x, y = pair
        return cls(x, y)  # cls(...), not Point(...) -- works right for subclasses too

    @staticmethod
    def distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


p1 = Point.from_tuple((0, 0))
p2 = Point.from_tuple((3, 4))
print(p1, p2)
print("distance:", Point.distance(p1, p2))


class Point3D(Point):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z


# from_tuple is inherited unchanged, but cls is Point3D here, so it builds a
# Point3D -- this is the payoff of using cls instead of hardcoding Point.
p3 = Point3D.from_tuple((1, 2))
print(type(p3).__name__, p3.x, p3.y)

print("---")


# Magic methods control how built-in operations behave on your objects.
# __repr__ is for developers (repr(obj), what you see in a REPL/debugger) --
# aim for something unambiguous, ideally re-creatable code. __str__ is for
# end users (print(obj), str(obj)) -- falls back to __repr__ if you don't
# define it. Defining __eq__ switches equality from identity (default,
# same as `is`) to value comparison -- but it also sets __hash__ to None
# unless you define __hash__ too, because a mutable object that can change
# its "equal" value would break dict/set lookups if it stayed hashable.
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __hash__(self):
        return hash((self.amount, self.currency))


m1 = Money(10, "USD")
m2 = Money(10, "USD")
print(repr(m1))       # uses __repr__
print(m1)              # uses __str__
print(m1 == m2)        # True -- value equality, even though they're different objects
print(m1 is m2)        # False -- still different identities
print({m1, m2})        # a set collapses them -- same hash + equal, so one survives
