# L2: Class-Related Decorators

"""
Decorators

Decorators are a powerful and helpful tool in Python because they allow
programmers to change the behaviour of a class or function. Decorators allow us
to wrap another function to extend the behaviour of the wrapped function
without permanently changing it. In Python, there are three decorators to
change the behaviour of class methods: @classmethod, @staticmethod,
@abstractmethod.
"""

"""
Class Methods

Unlike instance methods, class methods are not bound to a specific object.
Instead, they take the first arguments cls, which points to the class, not the
object instance. For this reason, they can't modify the state of the object
instance. But they can modify the class state using cls that will apply to all
class instances.
"""


class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

    @staticmethod
    def is_adult(age):
        return age > 18


"""
As you can see, the change_origin_country method is marked with the
@classmethod decorator, which tells Python that this is a class method. It is a
built-in decorator, so you don't need to import it.

Inside the method, you can change the class attribute origin_country to the new
one by accessing it through the cls parameter.
"""
Person.change_origin_country("UK")
obj = Person("Can", 26, "Male")
print(obj.origin_country)

"""
After changing the class origin_country attribute, the origin_country of the
class is also changed.
Class methods are often used to change some variables that belong to the class,
not specific objects. It can be very useful in some cases.
"""

"""
Static Methods

Static methods don't take a self or cls parameter, although they can take any
other arbitrary parameters. They can't modify either the object or class state.
The advantage of static methods is that they don't require object instantiation
before a call.
"""

"""
is_adult method is marked with a built-in decorator @staticmethod, which tells
Python that this method is static.
There is no self or cls argument, only an age attribute. This method returns
true if the age exceeds 18; otherwise, it will return false.
"""

print(Person.is_adult(19))
print(Person.is_adult(17))

"""
Property

Python's property function allows the turning of class attribute into
properties. It is a built-in decorator, so there is no need to import it.
"""


class Engineer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"


"""
Here you have a simple class with three attributes. If you create an object
from that class and try to modify the first_name attribute, will the email
attribute change as well?
"""
obj = Engineer("Alex", "Johnson")
print(obj.email)
obj.first_name = "Bob"
print(obj.email)

"""
email attribute has not been changed. It happens because our email attribute is
set up in the __init__() method and further modification to first_name or
last_name attributes will not affect the email attribute.

One way to resolve this might be to make an email() method.
This method works fine, but you will notice that email is no longer an
attribute. It's a method. To resolve this, you can use a property() decorator.
"""

"""
Abstract Base Classes (ABC)

An abstract class, or abstract base class (ABC), is a class that cannot be
instantiated because it is either labeled as abstract or it simply specifies
abstract methods. An abstract method means a method without implementation.
There is the Abstract Base Class (ABC) in Python for creating abstract classes.

Abstract classes are supposed to be inherited but avoid implementing methods,
leaving only method signatures that subclasses must implement.

Abstract classes are used in large projects where it is impossible to remember class details. Moreoever, code reusability can increase the chance. Therefore, it plays an essential role in these kinds of projects.
One of the simplest ways to create an abstract method in Python is to raise the
NotImplementedError exception from the method's body. It will prevent child classes from accessing parent methods without overriding them.
"""


from abc import ABC, abstractmethod


# Inherit from ABC to turn it into an abstract class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError("You have to implement eat() method")


class Dog(Animal):
    def eat(self):
        print("Dog is eating!")


# obj = Dog()
# obj.eat()

"""
But as it can be seen, you can create an object and get an error when you call
the eat() method. You can avoid this behaviour by using the abc module. Or if
you implement the behaviour of eat() method for all methods of the class.

Every class inherited from the Animal class must override the eat() method.
Otherwise, it will raise TypeError.
"""
obj = Dog()
obj.eat()

"""
The Abstract class can only be instantiated if it has at least one
@abstractmethod or @abstractproperty. Otherwise, it can't be instantiated and
would behave as a regular class.
"""
