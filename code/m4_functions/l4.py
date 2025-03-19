# L4: Lambda Functions

# In some cases, you might need one statement function used only in one place
# in your program. There is a lambda function in Python for such situations.
# The lambda function is an anonymous inline function consisting of a single
# expression which is evaluated when the function is called.

# There are the following templates for lambda functions:
# lambda arg1, ..., argN: <statement>
# Without arguments: lambda: <statement>

# As a a regular function, lambda receives a set of arguments as input. A
# statement is a legal Python expression. By default, lambda returns a result
# of the <statement>
# A lambda expression returns a pointer to the function, which can be assigned
# to a function name.

# Universal Function Expression
def sum_number(a, b):
    return a + b

# Usually, lambda is used when another function or method can get an input
# function object. For instance, it could be a sort method for the list object.
# The sort method can get a function as an input argument that returns one
# value for sorting

def main():
    # Lambda Expression
    sum_number_lambda = lambda a, b: a + b
    print(sum_number_lambda(1, 3))

    pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
    pairs.sort()
    print(pairs)

    # If you want to sort a list of tuples by text value, you can do it the
    # following way.

    def filter_function(pair_item):
        return pair_item[1]

    pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
    pairs.sort(key=filter_function)
    print(pairs)

    # Or you can use a lambda as a filter for sorting:
    pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
    pairs.sort(key=lambda x: x[1])
    print(pairs)

    # map(function, iterable) returns an iterator that applies a function to
    # every item of the iterable.
    # Imagine you need to square all elements of the list
    nums = [48, 6, 9, 21, 1]
    square_all = map(lambda x: x ** 2, nums)
    print(list(square_all))

    # filter(function, iterable) returns an iterator from elements of the
    # iterable for which the function returns True. If the function is None,
    # the identity function is assumed; that is, all elements of the iterable
    # that are false are removed.
    # Please, note the differences between filter(function, iterable) and
    # filter(None, iterable)
    # filter(function, iterable) is equivalent to function [item for item in
    # the iterable if function(item)]
    # filter(None, iterable) is equivalent to the condition [item for item in
    # the iterable if item]
    # For example, let's get only even numbers from the list.
    nums = [48, 6, 9, 21, 1, 35, 16, 12, 0, -1]
    print(list(filter(lambda x: x % 2 == 0, nums)))

    # In case you provide None as a function, there will be the following
    # result:
    print(list(filter(None, nums)))

    """
    functools.reduce(function, iterable, [, initializer])

    - Reduce applies a function of two arguments cumulatively to all iterables,
      from left to right.
    - Finally, it reduces the iterable to just a single value. For example,
      reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) calculates ((((1 + 2) + 3) +
      4) + 5). For the first iteration, reduce takes the first two items from
         the iterable. In our case, they are 1 and 2. Then it applies a
         function to them and treats a function result as the first item of the
         iterable instead of 1 and 2.
    """
    nums = [1, 2, 3, 4, 5]
    from functools import reduce
    print(reduce(lambda x, y: x + y, nums))

    # Note, if there is only one element in the iterable, it will be used as a
    # result.

    print(reduce(lambda x, y: x + y, [9]))

    # If the iterable is empty and the optional initializer argument is
    # present, reduce will return an initializer value
    print(reduce(lambda x, y: x + y, [], -1))

if __name__ == "__main__":
    main()
