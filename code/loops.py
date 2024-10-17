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
