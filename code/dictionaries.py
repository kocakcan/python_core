# A dictionary is a Python implementation of a data structure, commonly known
# as a hash table or associative array.

# A dictionary is an associative array where arbitrary keys are mapped to
# values. It's a mutable data type and may contain other data types and other
# dicitionaries as a value.

# A dictionary is represented with class dict.
# There are two ways to create a dictionary:

# Curly Braces
# You can use curly braces to create a dictionary. Pairs in the dictionary are
# seperated by commas. And a colon seperates the key from the value:
d = {
    "name": "Can",
    "age": 26,
    "is_registered": False,
    "rate": 12.5,
    "total_score": 200,
    "linked_ids": [1, 45, 98],
}
print(type(d))

# Built-In Function dict()
# An alternative way to initialize a dictionary is to use the built-in function
# dict():
d2 = dict([(1, "foo"), (10, "bar")])
print(d2)
# The dict() function can receive a sequence of key-value pairs--for example,
# a list of tuples.
# Also, you can proceed with dictionaries with the following operations:

# Access
# Dictionary items can be accessed by a key:
name = d["name"]
# If there is no such key, the interpreter raises an exception:
try:
    orders = d["orders"]
except KeyError:
    print("Such key does not exist.")

# Update
# The value can also be updated by a key:
d["age"] = 27

# If there is no such key, it will be added to the dictionary:
d["preferences"] = None

# Remove
# To remove a pair from the dictionary, use the del statement with an exact key
# to delete:
del d["preferences"]

# If there is no such key, the interpreter raises an exception:
try:
    del d["preferences"]
except KeyError:
    print("No such key exists.")

# The dictionary supports iteration by for loop:
for pair in d.items():
    print(pair)

# The same can be implemented in such a way:
for key, value in d.items():
    print((key, value))

# And membership check:
if "preferences" in d and d["preferences"]:
    print(d["preferences"])

# Dictionary keys can be objects of any hashable, an object with a hash value
# that stays the same throughout the lifetime of the object, data type.

# While many hashable types in Python are immutable (like int, float, str, and
# tuple), it is not a strict requirement that hashable types must be immutable.

# There is no limitation for dictionary values at all. They can contain any
# Python data type.

# Dictionary Manipulations
# The dict class has several useful built-in methods.

# get() method takes a key as a parameter and returns the value by this key.
# The method doesn't raise an error if the key doesn't exist:
print(d.get("preferences"))

# By default, it returns None if a key doesn't exist. But you can specify this
# value with an additional optional parameter:
print(d.get("preferences", "There is nothing!"))

# items() method returns the iterable object dict_items where each element is a
# tuple of the form (key, value):
for pair in d.items():
    print(pair)

# keys() and values() methods
# The keys() method returns a dict_keys object which contains keys from a
# dictionary and the values() method returns dict_values object with values of
# a dictionary. Both these objects are sequence objects:
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

# update() method takes another dictionary or some collection of key-value
# pairs as an argument and updates all matching pairs in the original
# dictionary and adds key-value pairs for keys that don't exist in the original
# dictionary:
blank_d = {
    "name": "",
    "age": 0,
    "is_registered": False,
    "rate": 0,
    "total_score": 0,
    "linked_ids": [],
}

d.update(blank_d)
print(d)

# Mutable types can't be used as dictionary keys such as lists, sets,
# dictionaries.
my_d = {
    "name": "Can",
    "age": 26,
    19: 25,
}

print(my_d["name"])
# Values that compare equal (such as 1, 1.0, and True) can be used
# interchangeably to index the same dictionary entry.
print(my_d[19])
print(my_d[19.0])

# class dict(**kwargs)
# class dict(mapping, **kwargs)
# class dict(iterable, **kwargs)
# Return a new dictionary initialized from an optional positional argument and
# a possible empty set of keyword arguments.

# Dictionaries can be created by several means:

# Use a comma-seperated list of key: value pairs within braces: {"jack": 4098,
# "sjoerd": 4127} or {4098: "jack", 4127: "sjoerd"}

# Use a dict comprehension: {}, {x: x ** 2 for x in range(10)}
# Use the type constructor: dict(), dict([("foo", 100), ("bar", 200)]),
# dict(foo=100, bar=200)

my_d = dict(name="Can", age=26)
for i, k in my_d.items():
    print(i, k)

print({i: i ** 2 for i in range(5)})

payload = {
    "url": "https://www.google.com",
    "Content-Type": "application/json",
    "auth": "some_bearer_token",
}

if "url" in payload and payload["url"]:
    print("It exists.")
