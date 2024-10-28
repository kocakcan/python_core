# Lists are the type of data structures in Python
# used to store multiple items in a single variable.

# Lists in Python are ordered mutable sequences, like arrays in other languages
# but dynamically sized. List items can be of any data type.

# To initiate list use square brackets.
my_first_list = ["Hello", 33, True, "everybody!"]
print(type(my_first_list))

# List items are indexed, starting from [0].
# The list is changeable and this can be achieved in two ways:
# You can change items by index:
my_first_list[2] = False
print(my_first_list)

# Or you can add new items to the list:
my_first_list.append(["something else..."])
print(my_first_list)

# Iterating and slicing work for a list the
# same way as for strings.
some_numbers = [1, 3, 5, 9, 11, 16, 28, 44.7, 90.6, 5334]
for i in some_numbers[::2]:
    print(i)

# sort - The list is ordered. So you can sort it by using the special sort as a variant.
some_numbers = [11, 5, 16, 28, 5334, 44.7, 90.6, 1, 3, 9]
some_numbers.sort()
print(some_numbers)

# You can get the list length by using the common method len.
print(len(some_numbers))

# The extend method allows you to add all the items from another iterable
# object, for example, from another list or string.
some_list = [1, 2, 3]
some_str = "abc"
some_list.extend(some_str)
print(some_list)

# Since the list data type allows for duplication, the count method allows you to count the
# number of times something appears in the list.
x = 1
some_list = [1, 2, 3, 2, 1, 1]
print(some_list.count(x))

# The pop method allows the removal and returning of items from a list by the given index.
# If an index is not specified, it removes and returns the last item in a list.
# This method allows the use of a list as a stack.
my_stack = [1, 2, 3]
my_stack.append(4)
my_stack.append(5)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

# A typical case in Python is when a list is initialized before some loop,
# and its items are filled in the loop according to some condition.
# For example, you need to find and store all even numbers from some sequence.
# At first glance, the following standard solution may be optimal:
n = int(input("Input integer number: "))
even_numbers = []
for i in range(1, n):
    if not i % 2:
        even_numbers.append(i)
print(even_numbers)

# But in Python, you can write the same functionality in just 3 lines
# using a special tool list comprehension.
n = int(input("Input integer number: "))
even_numbers = [i for i in range(1, n) if not i % 2]
print(even_numbers)

# new_list = [expression for item in iterable if condition == True]
