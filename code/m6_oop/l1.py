# L1: OOP Basics

"""
A programming paradigm is a way to classify programming languages based on
their features.

Object-oriented programming (OOP) is the programming paradigm that allows using
object-oriented analysis and design (OOAD) to model software design around
objects rather than logic or functions.

Objects are real-world entities that you can feel, manipulate and sense. For
example, an object can represent a person with the following properties: age,
name, gender, and behaviours like eating, sleeping, walking, etc.
"""

"""
Class vs. Instance

A class is a blueprint for the object. The class specifies attributes and
methods which the object will have. You can assume the class is a type of
object.

On the other hand, an instance is an object with actual information created
from a class. You can assume an instance is a particular object.
"""

"""
OOP Principles

OOP design is based on several concepts called OOP principles. These are
Abstraction, Encapsulation, Polymorphism, and Inheritance. These are also
called the four pillars of object-oriented programming.
"""

"""
Abstraction

Abstraction is one of the core concepts of OOP, which enables the user to
implement even more complex logic on top of the provided abstraction without
the need to understand or think about all the hidden background complexity.

Abstraction is a process of removing or generalizing physical, spatial, or
temporal details or attributes in the study of objects or systems to focus
attention on details of greater importance. Also, it is the creation of
abstract concept objects by mirroring common features or attributes of various
nonabstract objects or systems of study - the result of the process of
abstraction.

We all use cars, and we know that when we press on the gas, the car starts
moving and when we press the brake, the cars starts stopping. But we do not
know how these operations are happening in the background. We know about cars
and use a model of car with necessary functions.
"""

"""
Encapsulation

Encapsulation refers to the bundling of data with methods that operate on that
data or restricting the direct access to some of an object's components.

When a class is created, it means that encapsulation is automatically
implemented. This is because class binds instance variables and methods into a
single unit.
"""

"""
Polymorphism

Polymorphism is the provision of single-interface for entities of the different
types or the use of a single symbol to represent the several different types.

Polymorphism is a Greek word that means "poly" - many and "morph" - form. There
are two significant classes of polymorphism: parametric and ad-hoc
polymorphism.

Parametric polymorphism is a data type of function that can be written
generically to handle values differently without depending on their type.

Ad-hoc polymorphism refers to functions that can be applied to arguments of
various types. It behaves differently depending on the type of arguments they
are applied to. There is no ad-hoc polymorphism in Python.
"""

# One of the best examples of polymorphism is the addition of numbers.
a = 1 + 1
b = 1 + 1.0

# Here magic method __add__() receives different types of arguments and, based
# on this, returns different values.

"""
Inheritance

Inheritance is one of the most critical concepts in OOP, which simulates the
real-world concept of inheritance.

In terms of programming, inheritance is the mechanism of basing an object or
class upon another object or class, retaining a similar implementation.

The class which inherits the properties is called derived or the child class.
At the same time, the class from which it inherits is called the base or the
parent class. A class can inherit properties from another class, but it also
has its properties.
"""


class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")


class Employee(Person):
    def __init__(self, name, age, gender, salary, job_title):
        super().__init__(name, age, gender)
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Employee {self.name} works as a {self.job_title}")


# Here a new class Employee inherited from the Person class is created. In
# Python to inherit a class, you should write the parent class name inside
# brackets after writing the child class name, like class Employee(Person)
# In the __init__() method, the super keyword is used. It allows you to avoid
# writing the base class name explicitly. You can also write like
# Person.__init__(self, name, age, gender), and it will work the same way.
# The Employee class inherited all attributes from the Person class and has its
# method called display_info.

"""
There is a built-in issubclass(cls, class_or_tuple) method in Python, which
takes 2 argumnets cls, and class_or_tuple. This method returns True if cls is
derived from another class or is the same class. There is also built-in
isinstance(cls, class_or_tuple) to return whether an object is an instance of a
class or subclass. The super method is an essential part of Python that helps
us work with parent classes.
"""

"""
Data/Information Hiding

Data/information hiding is the principle of segregation of the design decisions
in a computer program that are most likely to change, thus protecting other
parts of the program from extensive modification if the design is changed. Data
or information hiding is usually implemented with the help of access modifiers.
Different programming languages can have a different number of access
modifiers.

Public: Everyone can access data
Private: The access can be achieved only with the class
Protected: Only class and subclass can access data

However, in Python, there are no such concepts. Instead, there is a simulation
of this mechanism. There are two types of access modifiers: protected and
private.

To denote an attribute as protected, you need to put one underscore _ before
the name of an attribute, while to mark an attribute as private, put double
underscore __.

However, Python does not guarantee privacy, and you can still access them. For
example, to access the protected variable, you need to put one underscore
before the attribute name. But to access the private attribute, you need to do
a little more work and access them in this syntax:
obj._ClassName__attributeName

If you try to access salary attributes by doing this, you will get
AttributeError saying Employee object has no attribute.
"""


class Employee(Person):
    def __init__(self, name, age, gender, salary, job_title):
        super().__init__(name, age, gender)
        self._job_title = job_title
        self.__salary = salary


obj = Employee("Can", 27, "Male", "$5000", "Software Engineer")
print(obj._Employee__salary)
# print(obj.__salary)

"""
Diamond Problem and Method Resolution Order

Python supports multiple inheritances, which means that the base class can
inherit from many parent classes. Diamond problem is an ambiguity that occurs
when two classes, Left and Right, inherit from the Base class and another Child
class inherits from both Left and Right.

        Base
     /       \
    Left    Right
    \         /
       Child
"""


class Base:
    def call(self):
        print("Base Class")


class Left(Base):
    def call(self):
        print("Left Class")


class Right(Base):
    def call(self):
        print("Right Class")


class Child(Left, Right):
    pass


obj2 = Child()
obj2.call()

"""
There is not an ideal algorithm for choosing Right or Left. This question is
called the diamond problem. Python knows which class call() method to invoke by
method resolution order (MRO). In Python, both built-in and user-defined
classes are inherited from the object class. And all the objects are instance
of the object class. If it's not found, it's searched in the parent classes.
The parent classes are searched from left to right order, and each class is
searched once. For this example above, the order will be the following:

    Child -> Left -> Right -> Base -> Object

Python uses C3 linearization to determine this order.
"""
