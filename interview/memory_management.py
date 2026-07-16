import sys
import gc
import copy

a = "hello world"
print(sys.getrefcount(a))   # 4

b = a
print(sys.getrefcount(a))   # 5, b points to a as well

del b
print(sys.getrefcount(a))   # should be 4

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)               # True  (same values)
print(a is b)               # False (different objects)
print(a is c)               # True  (same objects)
print(id(a), id(b), id(c))  # a and c share an address, b doesn't

# Mutable default argument bug
def add_item(item, my_list=None):
    # my_list.append(item)
    # return my_list
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))          # WTF?
print(add_item(3))          # WTF?

class Node:
    def __init__(self):
        self.other = None

a = Node()
b = Node()
a.other = b
b.other = a                 # circular reference: a -> b -> a

del a
del b                       # Reference counting alone CAN'T clean this up
                            # due to the cycle count never hits 0
                            # Python's cyclic garbage collector handles this
print(gc.collect())

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = "CHANGED"

print(shallow)
print(deep)

x = 256
y = 256
print(x is y)               # True

x = 257
y = 257
print(x is y)               # Depends
# CPython caches small ints (-5 to 256). Outside of the range depends on the
# implementation; If they are in the same code block then the result is True,
# but if they are in different code blocks then it's False. That's why you
# should never use is for integer comparison and always use ==
