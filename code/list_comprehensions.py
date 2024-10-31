# List comprehensions provide a concise way to create lists. Common appli-
# cations are to make new lists where each element is the result of some
# operations applied to each member of another sequence or iterable,
# or to create a subsequence of those elements that satisfy a certain
# condition.
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print(f"The loop counter is: {x}")

# Note that this creates (or overwrites) a variable named x that still exists
# after the loop completes. We can calculate the list of squares without any
# side effects using:
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# or, equivalently:
squares = [x**2 for x in range(10)]
print(squares)

# A list comprehension consists of brackets containing an expression followed
# by a for clause, then zero or more for or if clauses. The result will be a
# new list resulting from evaluating the expression in the context of the for
# and if clauses which follow it.
ex = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(ex)

# and it's equivalent to:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ["     banana      ", "    loganberry      ", "    passion fruit   "]
print([word.strip() for word in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# Note that the tuple must be paranthesized, otherwise an error is raised
# flatten a list using a listcomp with two "for"
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# List comprehesions can contain complex expressions and nested functions:
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

# The initial expression in a list comprehension can be any arbitrary
# expression, including another list comprehension.
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
]
# The following list comprehension will transpose rows and columns:
print([[row[i] for row in matrix] for i in range(4)])

# The inner list comprehension is evaluated in the context of the for that
# follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# which, in turn, is the same as:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# In the real word, you should prefer built-in functions to complex flow
# statements. The zip() function would do a great job for this use case.
print(list(zip(*matrix)))

# There is a way to remove an item from a list given its index instead of its
# value: the del statement. This differs from the pop() method which returns a
# value. The del statement can also be used to remove slices from a list or
# clear the entire list.
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
# same as a.clear()
del a[:]
print(a)
