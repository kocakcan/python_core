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

def spike():
    """Perfom spike."""
    print("Flying spike mate")

def main():
    spike()

if __name__ == "__main__":
    main()
