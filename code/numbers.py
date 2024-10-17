# The valid integer literals in Python can look like this.
a = 100
b = -10
y = 40000000000000000000000000000000000000

# Leading zeros are not allowed.
# x = 001234

# The int() function allows for converting string and float values to int.
x = "100"
y = int(x)
print(type(y))

# This can be useful when you input some value from the command line.
x = input("Please input some integer: ")
# This should be str
print(type(x))
# Convert the str into int and assign it to y
y = int(x)
# This should be int
print(type(y))

# Floating point numbers are also real numbers.
# They can be positive or negative with fractional part
# denoted by the decimal symbol or the scientific notation E or e
a = 7893.45
b = 5.244
c = -4.44
d = .32
e = 1.0e0

numbers = [a, b, c, d, e]

for number in numbers:
    print(f"{number} -> {type(number)}")

# Use float() to convert string, int to float.
x = "100"
y = float(x)
print(type(y))

# Complex numbers consist of two floating-point numbers
# representing real and imaginary parts
# Both parts are read-only and are accessed by .real, .imag attributes
# Represented by complex class, use complex() to convert a string containing# a complex number to complex type
x = "1+2j"
z = 50+3j
y = complex(x)
print(type(y))
print(z.real)
print(z.imag)

# Addition
print(17 + 5)
print(10.4 + 7)

# Subtraction
print(14 - 5)
print(13.4 - 8)

# Multiplication
print(4 * 4)
print(7 * 3.2)
print(-2 * 12)

# Division
print(16 / 4)
print(5 / 2)

# Modulus
print(6 % 2)
print(7 % 2)
print(13.2 % 5)

# Exponentiation
print(2 ** 2)
print(2 ** 3)
print(-3 ** 2)
print((-3) ** 2)

# Floor Division
print(12 // 5)
print(4 // 3)
print(25 // 6)

c = 5 + 10
b = 3
a = c / b

# The result of the division is always a floating-point number
x = 10 + 30 + 6 / 3
print(x)

# Use parantheses as a priority operator to indicate the precedence of operations.
x = (10 + 30 + 6) / 3
print(x)

# Heron's formula
import math
a = 5
b = 2.5
c = 4
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)

# Classic Incrementation
a = 1
a = a + 1

# Shorter Incrementation
a += 1  # instead of a = a + 1

# Degrees are first converted to radians
# Then we can get the cosine
angle_degrees = 60
angle_radians = math.radians(angle_degrees)
print(math.cos(angle_radians))

# Euclidean distance
x = 4
y = 5
print("Euclidean distance for x =", x, " y =", y, "hypot=", math.hypot(x, y))

# acos(x) - Arc cosine
# asin(x) - Arc sine
# atan(x) - Arc tangent
# sqrt(x) - Square root
# hypot(x) - Euclidean distance: sqrt(x ** 2 + y ** 2)
# sin(x) - sine
# tan(x) - tangent
# degrees(x) - radians to degrees
# isnan(x) - check if x is a number

# random module provides functions for generating
# random numbers, letters, and random selection
# elements from sequences
# generated numbers are pseudorandom numbers, meaning
# they are not truly random but "random enough"

import random
x = 0
y = 6
print(random.randint(x, y))
print(random.randint(x, y))
print(random.randint(x, y))

# choice(sequence) - returns a random element of a non-empty sequence
# randrange(start, stop, step) - returns a randomly selected number from a sequence
# random() - returns a random number from 0 to 1.
# seed([a], version=2) - the initialization of the random number generator. If a is not specified, the system is used.
# shuffle(sequence, [rand]) - shuffles the sequence (changes the sequence itself). Therefore, the function does not work for immutable objects.
# uniform(x, y) - returns a random floating-point number from x to y.
