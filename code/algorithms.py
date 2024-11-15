# A dictionary is a very common collection type in Python. You may encounter
# this in almost every project. These are following main advantages of the
# dictionary: flexibility, simplicity, and performance.

# Key access is very fast when you are dealing with dictionaries. But the time
# for the operation is not the main thing. It's all about algorithmic
# complexity.

# Algorithmic complexity measures how long an algorithm would take to complete
# given an input of size n.

"""
    And the most common metric for calculating time complexity is the Big O
    notation. It describes how long the order of number of operations task
    would take to complete it.

    The Big O notation is a mathematical notation used to classify algorithms
    according to how the number of iterations changes as the input data grows.

    The running time itself depends on external parameters, for example, the
    characteristics of the machine on which the program code is running. But at
    the same time, the number of iterations remain unchangeable. This is
    because it depends only on the algorithm itself.
"""

# O(n!) Factorial complexity - Permutations of a string
# O(2^n) Exponential complexity - Finding all the subsets on a set, Fibonacci 
# O(n^2) Quadratic complexity - Bubble sort, insertion sort, or selection sort
# O(nlogn) Linearithmic complexity - Merge sort, quicksort, and others
# O(n) Linear complexity - Getting the max/min value in an array
# O(logn) Logarithmic complexity - Binary search
# O(1) Constant complexity - Array item access by index
# Algorithmic complexity for accessing array items by index is O(1) and this is
# one of the most valuable features of an array.

# Hash Table
# Access by a key to an element of a dictionary in most cases is approximately
# O(1).
# To understand why it's "approximately O(1)", you have to look at the internal
# structure of a hash table.

# A hash table is a data structure that stores a collection of key-value pairs.
# There are two main parts that are essential to understanding how a hash table
# works.

# First, hash table data is stored in an array. And that's why element access
# is so efficient. Because access to an item by index in an array is, the Big O
# definition O(1).

# Second, the hash function allows us to associate a key with some index in the
# array. That's why a dictionary key can only be of a hashable type. The hash
# function returns some integer value for each hashable object.

"""
    Ideally, we should get a unique index for each key using a hash function.
    But this part of the description is significantly simplified. In fact, hash
    values of different keys may have duplicates. They are called collisions.
    There are several different ways to solve collisions. But this is why
    sometimes the Big O definition for an access item by key in a hash table is
    not O(1).

    The main disadvantage of using a dictionary is also related to one of the
    approaches to resolving collisions. Usually, the data storage array is
    larger than the actual amount of data. So, dictionaries are not very
    effective in memory use.
    For memory optimizations purposes, a common alternative to a dictionary is
    the named tuple data type.
"""

"""
    A dictionary type is a Python implementation of a data structure, more
    commonly known as a hash table or associative array. A dictionary is a
    collection of key-value pair items. It is mutable and dynamic. A dictionary
    can grow and shrink. It may be nested and contain other collection data
    types and other dictionaries.

    There are two ways to create a dictionary: you can use curly braces or the
    built-in function dict(). The dictionary keys can be objects of any
    hashable data type. And there is no limitation for dictionary values at
    all.

    The main advantages of the dictionary are flexibility, simplicity, and
    performance. The key access is very fast when you are dealing with
    dictionaries. Constant complexity O(1) can be used to describe the access
    by key to an element of a dictionary. To understand why it is so, you have
    to look at the internal structure of a hash table. Two main parts are
    essential to understanding how a hash table works. First, hash table data
    is stored in an array. Second, the hash function allows us to associate a
    key with some index in the array.
"""
