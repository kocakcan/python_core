# L5: Recursions
# In Python, a function can call other functions. But, even more, the function
# can call itself.

# In computer science, recursion is a method of solving a computational problem
# where the solution depends on solutions to smaller instances of the same
# problem. Recursion solves such recursive problems by using functions that
# call themselves from their own code. Corresponding functions are called
# recursive functions.

# Recursion is always compared with loops functionality in Python. There are
# many different types of loops. But in a nutshell, almost each of them has the
# same basic--loops iterates through the data to analyze or manipulate it.
# For that reason, recursion is just another type of loop. Almost all recursive
# functions can be re-written as loops and vice versa.

# Recursion is a fantastic way to solve some problems, such as math and
# algorithms. For a mathematician, the first association with recursion is a
# fractal.

# Recursion has two required conditions for a successful ending:
# 1. A defined base case or exit condition (one or more). The base case is the
#    problem with a predefined answer that can be solved without more recursive
#    calls.
# 2. A recursive call should only be made with a changed input argument value.

# There is the following structure of the recursion function:
# def function_name(arg):
#     <base_case>                     # do not need to calculate, return predefined value
#     function_name(<modified_arg>)   # recursive call with the changed argument


# A good example of using recursion is the Fibonnacci sequence. The
# Fibonnacci sequence is a sequence where the first number is 0, the second
# number is 1, and the N^th number is the sum of the (N-1) and (N-2).
# So, the task is to write a function calculating the N^th element of a
# sequence.

# You can solve this task with an ordinary loop:
# def get_fib(n):
#     n_fib = None
#
#     if n < 1:
#         print("N must be > 0")
#     elif n == 1:
#         n_fib = 0
#     elif n == 2:
#         n_fib = 1
#     else:
#         prev_2, prev_1 = 0, 1
#         for i in range(2, n):
#             n_fib = prev_2 + prev_1
#             prev_2 = prev_1
#             prev_1 = n_fib
#
#     return n_fib

# Without Base Cases
# You will get infinite recursion. For such case in Python, you will receive a
# RecursionError: maximum recursion depth exceeded.
# def get_fib(n):
#     return get_fib(n - 2) + get_fib(n - 1)


# Unchanged Input Argument
# The same will happen if you forget to change the input argument:
def fib_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Should pass in something other than the argument itself
        # such as n - 1
        return fib_num(n) + fib_num(n - 1)


#
def get_fib(n):
    """Get a Nth element of the Fibonnacci sequence."""
    if n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        value = get_fib(n - 1) + get_fib(n - 2)

    return value


# There are several pros and cons of using recursive functions.
# The biggest con is that the recursion functions use a lot of space.
# Each recursion call will be added to the call stack
# Stack would look like this for get_fib(5):
# main -> get_fib(5) -> get_fib(3) -> get_fib(1) -> get_fib(2) -> get_fib(4) ->
#         get_fib(2) -> get_fib(3) -> get_fib(1) -> get_fib(2)

# Advantages
# - recursive functions can make the code more elegant;
# - a complex task can be broken down into simpler sub-problems;
# - the sequence generation is easier than using some nested iteration.

# Drawbacks
# - quite ofthen the logic behind recursion is hard to follow and understand;
# - recursive calls are expensive (inefficient) as they take up a lot of memory
#   and time;
# - it is hard to debug;
# - there is a default value for the max number of recursion calls in Ptyhon.


def main():
    print(get_fib(10))


if __name__ == "__main__":
    main()
