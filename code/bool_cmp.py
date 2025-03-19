# To write some logical expressions, one should combine
# comparison and boolean operators.
# Boolean operators allow for defining logical expressions
# or can be used by control flow statements.
# Comparison operators provide different options for comparing values with each other.
# The result of logical expressions is always defined as True or False.
# Python has three boolean operators and, or, and not.
result = 3 >= 1 and 10 < 20
result_2 = 3 >= 1 or 10 < 20
result_3 = True
print(result)
print(result_2)
print(not result_3)

# Comparison operators
a = "a"
b = "a"
print(a == b)

a = True
b = False
print(a != b)

a = 4
b = 1
print(a > b)

a = 1
b = 1.5
print(a < b)

a = 1
b = 1
print(a >= b)

a = 1
b = 2
print(a <= b)

# Parantheses can be used to set precedence or to group operators
# to enhance readability
# result = (a >= minimum and b >= minimum) or minimum == 0

# You can also split a complex expression into multiple variables
# with different logical expressions and then use them in one expression
# expression1 = (a > b and a < c) or limit == 0
# expression2 = x <= y or x <= z or x <= g
# result = expression1 or expression2

# Python uses lazy evaluation meaning if there are several operators
# we would get the result from the first False or True statement
# and the interpreter won't compute the others.
a = 10
result = a < 10 and a < 20 and a > 5 and a % 5 == 0
# The result is returned from the first statements a < 10

# Logical expressions are used when you want to perform certain operations
# but only in case some conditions are satisfied.
a = 20
b = 33
minimum = 3
if a >= minimum and b >= minimum:
    result = (a + b) * 2
else:
    result = 0
print(result)

a = 20
b = 33
minimum = 0
if (a >= minimum and b >= minimum) and minimum != 0:
    result = (a + b) * 2
elif minimum == 0:
    print("The minimum value is not defined!")
    result = 0
else:
    result = 1
print(result)

my_operation = "read"
if my_operation == "read":
    print("perform read operation.")
elif my_operation == "update":
    print("perform update operation.")
elif my_operation == "insert":
    print("perform insert operation.")
elif my_operation == "delete":
    print("perform delete operation.")
else:
    print("wrong variant if operation !!! ")

match my_operation:
    case "read":
        print("perform read operation...")
    case "update":
        print("perform update operation...")
    case "insert":
        print("perform insert operation...")
    case "delete":
        print("perform delete operation...")
    case _:
        print("wrong variant if operation !!! ")

# Ternary operator can be used to simplify a representation of if/else expression.
# Has the following format x if C else y
fruit = "apple"
if fruit == "apple":
    is_apple = "Yes"
else:
    is_apple = "No"
print(is_apple)

fruit = "apple"
is_apple = "Yes" if fruit == "apple" else "No"
print(is_apple)

# The Boolean type in Python contains only two values: True and False.
result = 2 > 1 and 1 < 2
print(type(result))

# Boolean type is represented by bool class.
# Anything can be converted to bool. This is important as it happens everytime in logical expressions albeit not explicitly, allowing us to simplify our code significantly.
if x == 0:
    print("x is zero!")
elif x != 0:
    print("x is not zero!")

# Instead of this, we can write
if not x:
    print("x is zero!")
elif x:
    print("x is not zero!")

# Python will convert x to a bool by itself. So you only have to use the not boolean operator in the first case.
# This is because 0 will convert to False, while any number that is not 0 will convert to True.

# Sometimes, in cases where you don't have a value, you may want to fill your variables with explicit meaning "there is nothing here".
# For this purpose, Python provide a special type called None.
nothing = None
print(type(nothing))

# None can be used in logical expressions
# Instead of == comparison, None is usually checked with the help of is opearator. Just as:
if not x:
    print("x is None!")
elif x:
    print("x is not None!")
