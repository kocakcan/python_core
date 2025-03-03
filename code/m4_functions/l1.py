# A function is a series of statements which return some value to a caller.
# It can also be passed zero or more arguments which may be used in the
# execution of the body.

# Example Without a Return Statement

# def power(num_1, num_2):    # get input value
#     result = num_1 ** num_2 # perform calculation
#     return result           # provide the result

# The main reason for using functions is to reduce code duplications and
# simplify further code updates.
# If the code logic needs to be updated later, you only have one function to
# update. In other words, functions are used to maximize code reuse and
# minimize code redundancy.

# The main template for creating a function in Python is:
# def <function_name>(arg1, arg2,... argN):
#   <statements>

# Return keyword is optional, functions return None object.
# Only def keyword, function name, and at least one statement are required to define a function.

# If you haven't decided what to put in the function body, you can provide a
# docstring or pass keyword.

# First-Class Functions
# "A first-class entity (type, function, object, or value) is an entity which
# supports all the operations generally available to other entities."
#
# As you already know, in Python, everything is an object. For that reason, it is
# possible to talk about functions as first-class entities, or first-class
# functions, that support all object operations:
#     - assigning them to variables
#     - passing functions as arguments
#     - storing them in data structures
#     - returning them

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def apply_func(func, *args):
    results = []
    for arg in args:
        results.append(func(arg))

    return results

def get_func(func_name):
    func_mapping = {
        "square": square,
        "cube": cube,
    }

    return func_mapping.get(func_name, None)

class People:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __what__(self):
        print(f"{self.name} says hello")

def main():
    can = People("Can", 27)

    print(f"My name is {can.name}")
    can.__what__()

    print(square(5))
    # assign a function to a variable
    my_func = square
    print(my_func(19))

    # use my_func(square function) as an argument
    print(apply_func(my_func, 3, 5, 6))

    # Functions can be stored in data structures
    func_mapping = {
        "square": square,
        "cube": cube,
    }

    # This should print out 256
    print(func_mapping["square"](16))

    # Functions can be returned from other functions
    other_func = get_func(square)

    print(other_func(245))
if __name__ == "__main__":
    main()
