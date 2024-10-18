# x = int(input("Please input 0 to stop iteration: "))
# sum_result = 0
# equivalent to while True:
# while x:
    # sum_result += x
    # x = int(input("Please input 0 to stop iteration :"))
# print(sum_result)

# Operator continue allows you to move on to the next iteration, depending on some condition.
#   n = int(input("Input integer number: "))
#   sum_result = 0
#   x = 1
#
#   while x < n:
#       x += 1
#       if x % 2:
#           continue
#       sum_result += x
#
#   print(f"Sum of even numbers: {sum_result}")

# Operator break allows interrupt loops.
#   x = int(input("Input integer number: "))
#   is_prime = True
#   div = 2
#
#   while div < x:
#       if not x % div:
#           is_prime = False
#           break
#       div += 1
#
#   if is_prime:
#       print("Prime")
#   else:
#       print("Not prime")

# With the while loop, we can also use the else operator to run some code
# once the condition is no longer True
x = 1
while x < 5:
    print(x)
    x += 1
else:
    print("Loop was stopped at:")
    print(x)

for i in range(5):
    print(i)

# for operator is designed to use sequences and collections.
# That's why we can use the built-in function range
# that generates a sequence of numbers and the loop iterates
# with each item from this sequence.
# Using for in Python simplifies the code compared to using while
# We don't need to initiate counters before the loop
# and don't care about incrementing counters.
x = int(input("Input integer number: "))
is_prime = True
for div in range(2, x):
    if not x % div:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")

# We can also use continue, break, and else operators as we did in while loops.
x = int(input("Input integer number: "))

for div in range(2, x):
    if not x % div:
        print("Not prime")
        break
else:
    print("Prime")
# Because the else statement works only if the break operator is not executed
# it helps to avoid redundant variables and makes code simpler.

# Iterators are quite important in Python as for statement can be used with any iterable object.
# In other words, with any object that implements the iterator protocol.

# "Iterable" - an object capable of returning its members one at a time.
# Examples of iterables include all sequence types (such as list, str, and tuple)
# and some non sequence types like dict, file objects, and any objects of any
# classes we define with an __iter__() method or with a __getitem__() method that
# implements Sequence semantics.

# "Iterator" - an object representing a stream of data. Repeated calls to the iterator's
# __next__() method (or passing it to the built-in function next() return successive items
# in the stream. When no more data are available, a StopIteration exception is raised instead.
