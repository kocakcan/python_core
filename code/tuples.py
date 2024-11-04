# Generally, the tuple data type has the same characteristics as the list data
# type. It is ordered, can contain any other data types, and can be nested to
# an arbitrary depth. The items of tuples can also be accessed by index.
# There is one significant difference - tuples are immutable. It means that you
# cannot change the tuple after it has been instantiated.

# There are two ways to initiate a tuple:
# First, to create a tuple, you can use parantheses:
my_colours = ("Red", "Green", "Yellow", "White", "Black")
print(type(my_colours))

# Or you can create a tuple without parantheses, and it will work too:
fav_bosses = "Artorias", "Lady Maria", "Sir Alonne"
print(type(fav_bosses))

# When you initiate an empty tuple it works correctly - Python will create an
# object with the tuple type.
empty_tuple = ()
print(type(empty_tuple))

# But in the case of one element, you will get an integer. This is because
# parantheses are used as a precedence operator and the Python interpreter
# understands it as an arithmetic expression.
it_should_be_tuple = (1)
print(type(it_should_be_tuple))

# To create a tuple with one element, you must add an extra comma at the end:
it_should_be_tuple = (1,)
print(type(it_should_be_tuple))

# You can process tuples as you would lists or strings.
# You can iterate over them.
my_tuple = (5.5, True, "Some string", (1, 2, 3))
for item in my_tuple:
    print(item)

# You can indexes.
print(my_tuple[0])

# Tuple packing and unpacking are often done implicitly in Python.
# When one tuple is assigned to another, the variables are initialized in one
# line of code.
a, b, c = 40, 55.6, 90
print(a, b, c)

# It happens because the tuple is implicitly split into the seperate values.

# It is called an unpacking operation.
# You can reproduce this with a special unpacking operator *.
my_tuple = 40, 55.6, 90
print(my_tuple)
print(*my_tuple)
# Note that in the second case, with the * operator at the beginning, the
# seperated values were printed, as they were sent to the print function
# seperately by commas.

(a, b, c) = (40, 56.6, 90)
# Here, the tuple (a, b, c) is formed by the opposite operation, called the
# packing operation when the seperated values are collected into one. And
# because the tuple items are written as variables, these variables are
# initialized.
# Remember, you can omit the parantheses so it could look even better.
a, b, c = 40, 56.6, 90

# Remember, it will only work with the same count items/variables.

# Swapping Two Values
# Usually, this task can be solved with an additional, temporary variable:
a, b = 1, 2
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# But in Python, it can be solved much easier thanks to unpacking and packing.
# Then, only one action instead of three is the best solution,
a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)

# The result is expectable. During the checking, Python compares each item from
# both tuples. But in fact, there is only one tuple, only one object in memory,
# You can check it with the built-in function id:
print(id(x), id(y))

# As you can see, both variables are connected with the same object in the
# memory - the identification number is the same.
# It's because a tuple is an immutable type. And Python uses this approach as
# part of memory management, not only with tuples. As a result, the Python
# interpreter does not create a duplicate of the tuple in memory for optimizing
# purposes. You can use id(x) == id(y) to check whether two variables are
# connected with one object or not.
# But it's more convenient to use a special operator is for this purpose.
x = 1, 2, 3
y = 1, 2, 3
print(x == y)
print(id(x), id(y))
print(x is y)

# Again, because a tuple is an immutable type, both variables are connected
# with the same object in the memory,

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a), id(b))
print(a is b)

# A list is a mutable type. And for this reason, lists are equal but not
# connected with the same object in the memory.

# As was said before, it's done for memory management. But immutable objects
# with the same value are not always the same object in memory.
x = 2 ** 100
y = 2 ** 100
print(x == y)
print(id(x), id(y))
print(x is y)

x = (1, 2, "python" * 1000)
y = (1, 2, "python" * 1000)
print(x == y)
print(id(x), id(y))
print(x is y)

# Here it's better to say that two objects with non-overlapping lifetimes may
# have the same id() value.
