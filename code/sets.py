# A set is another collection data type in Python. Sets are mutable and dynamic
# like lists. But they are unordered, duplicates are not allowed, and can
# contain only hashable objects.

# To create a set, you should use the special built-in function
# set(<iterable>):
my_set = set((1, 113.5, True, "Some string"))

# As you can see, the set allows for the containing of different types in one
# collection. Note, you must send some iterable objects to the function, for
# example, some kind of collection. So, a tuple is sent as an argument.

print(type(my_set))
# Note, if you need to work with sets like an immutable type, you can use a
# frozenset data type.

# Also, you can initiate a set using curly braces:
my_set = {1, 113.5, True, "Some string"}
print(type(my_set))

# But you should consider that you will not get a set if you initialize an
# empty set with curly braces.

# Curly braces without data will initialize a dictionary:
my_set = {}
print(type(my_set))     # dict
# So, for this purpose, you must use the function set.
my_set = set()
print(type(my_set))

# That's because curly braces are also used to initialize dictionaries. And in
# this case, without data, Python creates exactly a dictionary.

# There is another important point about the set function. If you send to the
# function a list with duplicates, for example, then you will get a collection
# with unique items. It is because sets cannot contain duplicates.
my_set = set([1, 2, 3, 1, 2])
print(my_set)

# Sets are iterable but do not record element position or order of insertion.
# Accordingly, sets do not support indexing, slicing, or other sequence-like
# behaviour.

# You can iterate over the elements of sets with a for loop just as you would
# with lists or tuples.
for item in my_set:
    print(item)

# There is no arbitrary access to the elements of sets through indexes because
# they are unordered.
# print(my_set[1])

# Membership
if 1 in my_set:
    pass

# Length of set
print(len(my_set))

# Everything in Python is an object. So, an object in Python can be considered
# hashable if the class of this object implements a few special methods that
# allow getting a hash value.

# A hash value is used for identifying data.
# All immutable types in Python are also hashable. However, some custom types
# can be mutable and hashable at one time. It depends on the implementation of
# their classes.

# If the object is hashable, you can use a special built-in function hash to
# get the hash value for the object:

# Because tuple is an immutable, you can get a hash value for this object:
some_tuple = 1, 2, 3
print(hash(some_tuple))

# As you can see, a hash is just some integer value. Most importantly, this
# value will be unchanged, even if the internal state of the object has
# changed.

# Set Manipulations
# Set operations in Python can be performed in two different ways: by operators
# or methods.

# Union Operation
# with operator:
s1 = {'a', 'd', 'h'}
s2 = {'n', 'b', 'c', 'd'}
s3 = {'c', 'd'}
union = s1 | s2 | s3
print(union)
# with method:
union = s1.union(s2, s3)
print(union)

# Intersection Operation
# with operator:
s1 = {'a', 'd', 'h'}
s2 = {'n', 'b', 'c', 'd', 'a'}
s3 = {'n', 'a', 'd'}
my_intersection = s1 & s2 & s3
print(my_intersection)
# with method:
my_intersection = s1.intersection(s2, s3)
print(my_intersection)

# Difference Operation
# with operator:
s1 = {'a', 'd', 'h', 'c', 'j'}
s2 = {'n', 'b', 'c', 'd', 'a'}
s3 = {'n', 'a', 'd'}
my_difference = s1 - s2 - s3
print(my_difference)
# with method:
my_difference = s1.difference(s2, s3)
print(my_difference)
# The result set contains items from the first set that are not presented in
# other sets.

# As it can be seen from he examples above, the results are similar for
# operators and methods when working only with sets. But there is a difference
# when you need to work with any iterable type as an argument, for example,
# sets and lists.

# The operator works only with sets.
s1 = {'a', 'd', 'h'}
s2 = {'n', 'b', 'c', 'd'}
s3 = ['c', 'd']
# union = s1 | s2 | s3
# print(union)

# The method can take any iterable type as an argument.
union = s1.union(s2, s3)
print(union)

# A set is changeable, and there are a few methods for this purpose:
# The update method changes the value of the original set to the union with the
# specified sets:
s1 = {'a', 'b', 'k'}
s2 = {'a', 'd', 'h'}
s3 = {'n', 'b', 'd'}
print(f"s1 is {s1}")
s1.update(s2, s3)
print(f"s1 is {s1}")
# The intersection_update and the difference_update methods work similarly, but
# with intersection and difference, respectively.

# Also, you can just add an item to the set, or remove it.
s1 = {'a', 'd', 'h'}
print(s1)
s1.add("some string")
s1.remove('a')

# Or you can clear set at all:
s1.clear()
print(s1)
print(s1)

# A set is a useful type when dealing with collections without
# duplicates--especially if you need to compare them, find differences or check
# if there is something in common. For these purposes, the set provides useful
# and fast methods.

# Sets don't have a guaranteed order so aren't feasible for general use.
# Sets are significantly faster in membership checks.
