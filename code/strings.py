# Strings are immutable sequences of Unicode code points.
# A string is one or more characters enclosed in single or double quotes.
# Class str represents the data type string in Python.
print(type('A'))
print(type("Hello"))
print(type("""Three double quotes"""))
print(type('''Three double quotes'''))

# There is no particular character data type in Python.
# A single character is a string with a length of 1.
my_str = "This is a string"

# Also, we can use some special symbols.
# Backslashes can be used to escape special characters.
first_string = "This is \"double quotes\" in double quotes"
second_string = 'This is \'single quotes\' in single quotes'
not_new_line = "String without a new \\n line"
long_str = "Lorem ipsum, dolor sit amet, \
        sed do eiusmod tempor incididunt ut."

# Use \n to mark the new line start
print("There will be a new line\n here")

# Use \r to mark the carriage return.
print("Not this \r Only this!")

# It's easy to input a string from the CLI and print it out in the CLI
value = input("Enter some string:")
print(value)

# After reassigning a variable, it has a reference to another object.
# proving string are immutable.
my_str = "Hello"
print(id(my_str))
my_str = '!'
print(id(my_str))

# A string is an immutable sequence of characters.
# We can get characters from a string by index.
my_str = "Hello"
print(my_str[1])

# But we can't change a string value as they are immutable.
# my_str[1] = '!'

# We can iterate over strings are they are sequences.
for i in my_str:
    print(i)

# Python has advanced slicing functionality from strings and other sequences
# such as tuples, lists, ranges, or bytes. To achieve this use built-in
# function slice with the following syntax: slice([start], [stop], [step])
# The slice function returns a special object that we can use intead of specifying an index.
my_str = "Hello"
slice_object = slice(1, 3)
print(type(slice_object))
print(my_str[slice_object])

# But we can use simplified syntax, and it's enough to specify start, stop, and step
# indexes seperated by a colon.
my_str = "Hello"
print(my_str[1:3])

# This is an example of how to revert a string. The step point is set up to -1.
# Python interprets the slice like every item from the end to the beginning.
print(my_str[::-1])

# This example gets the string without the first and last elements. The start point is
# set to 1 (because the first item has an index of 0). The stop point is set to -1,
# which means the second item from the end.
print(my_str[1:-1])

# This example gets two symbols from the beginning. The start point is omitted, so it starts
# from the beginning and stop point is set up to 2, so it stops on the second item from the
# beginning as stop is exclusive.
print(my_str[:-2])

# This example gets the last symbol. Stop and step points are omitted. The start point is set
# to -1. When the start is less than 0, it starts counting from the end.
print(my_str[-1])

# split method takes another string as a seperator and returns a list of parts of the string.
my_str = "Hello-world"
for i in my_str.split('-'):
    print(i)

# The upper and lower methods return string converted into upper and lowercase:
print(my_str.upper())
print(my_str.lower())

# The find method searches a specified substring and returns the start position of this substring or - 1, meaning not found.
print(my_str.find("world"))

# The strip method returns a string without leading and trailing spaces
my_str = " Hello-world "
print(my_str.strip())

# Even though Python supports string concatenation, it does not work with
# different types and requires conversion to string.
age = 26
name = "Can"
location = "Turkey"

message = "Hello, my name is " + name + ", I am " + str(age) + ", I am from " + location
print(message)

# A better choice to use the format method instead of concatenation.
message = "Hello, my name is {}, I am {}, I am from {}".format(name, age, location)
print(message)

# Or we can use f-string syntax.
message = f"Hello, my name is {name}, I am {age}, I am from {location}"
print(message)

message = "The price is {price:.2f} dollars."
print(message.format(price=29))

# In case you need to check the occurrence of one string in another
# you can create conditional construct with the in operator.
message = input()
if "Hello" in message or "Hi" in message:
    print("It is greeting, we know")
