# Arguments are specified inside the parantheses and are comma seperated.
# Arbitrary number of arguments can be passed to functions.

def sum_number(a, b):
    print(f"{a} + {b} = {a + b}")

def sub_number(minuend, subtrahend):
    print(f"{minuend} - {subtrahend} = {minuend - subtrahend}")

def calc_value(minuend, subtrahend, degree):
    value = (minuend - subtrahend) ** degree
    print(f"({minuend} - {subtrahend}) ^ {degree} = {value}")

def show_arguments(*args, **kwargs):
    print(f"args: {args}; kwargs: {kwargs}")

def show_arguments_(*args, **kwargs):
    print(args[1:-1])
    print(kwargs["name"])

def show_unpacked_arguments(a, b, c, d, e):
    print(a, b, c, d, e)

def foo(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2='default', *args,
kwd_only1, kwd_only2='default', **kwargs):
    print(
        f"pos1={pos1}",
        f"pos2={pos2}",
        f"pos_or_kwd1={pos_or_kwd1}",
        f"pos_or_kwd2={pos_or_kwd2}",
        f"args={args}",
        f"kwd_only1={kwd_only1}",
        f"kwd_only2={kwd_only2}",
        f"kwargs={kwargs}",
        sep="\n",
    )

def test(value, arg_list=[]):
  arg_list.append(value)
  print(f'Inside the function: {arg_list}')

def main():
    # Arguments can be provided by position or name
    # Positional means that the order of providing arguments while calling a
    # function is significant.
    # For instance:
    sub_number(3, 1)
    sub_number(1, 3)

    # Keyword arguments match by the argument name
    sub_number(minuend=3, subtrahend=1)
    sub_number(subtrahend=1, minuend=3)

    # Different types of arguments can be used together provided all the
    # positional arguments are passed before keyword ones.
    calc_value(5, degree=2, subtrahend=1)
    sum_number(b=3, a=1)

    # Arguments can also be required or optional.
    # Optional arguments should be defined with a default value and can be
    # skipped when calling a function.
    # Note that first you should define all required arguments and then all
    # arguments with a default value. Order matters.

    # If you don't know how many positional and keyword arguments should be
    # provided, a function developer can pack input arguments:
    # Positional - to a tuple with one asterisk symbol
    # Keywords - to a dictionary with two asterisk symbols
    # Usually packed positional argument names args, keywords - kwargs.
    show_arguments(1, "name", arg1=[1, 2, 3], arg2="value")
    show_arguments_(1, "name", "value", 10, name="arg1", arg2="Tom")

    # In the example above, arguments 1, "name", arg1=[1, 2, 3], arg2="value"
    # are packed into the two variables: args and kwargs. These arguments are
    # packed in the function definition.

    # An argument can also be unpacked for a function call using the same
    # symbols as for packing arguments.
    list_of_args = [1, 2, "name"]
    key_value_args = {'e': "value", 'd': 3}
    show_unpacked_arguments(*list_of_args, **key_value_args)

    # The example above is equal to:
    show_unpacked_arguments(1, 2, "name", e="value", d=3)

    # The function show_unpacked_arguments has a finite set of input arguments.
    # All arguments can be passed one by one or unpacked from the other
    # variables. Variables are unpacked in the function call.

    # Positional only arguments can be specified with a slash / symbol.
    # Keyword-only parameters can be specified with a single asterisk *.
    # foo(1, 2, 3)
    foo(1, 2, 3, kwd_only1=4)
    foo(1, 2, 3, kwd_only1=4, kwarg1=5, kwarg2="it is a kwarg too")
    foo(1, 2, 3, "not default", kwd_only1=4, kwd_only2="not default", kwarg1=5,
        kwarg2="it is a kwarg too")
    foo(1, 2, 3, "not default", 6, "it is an arg too", kwd_only1=4,
        kwd_only2="not default", kwarg1=5, kwarg2="it is a kwarg too")

    # Functions can be: position, position only, position with default
    # keyword, keyword only, keyword with default
    
    # In Python, mutable objects are passed to a function by reference.
    # Immutable objects are passed to a function by value.
    # When passing parameters "by reference", a reference to an object is
    # passed through where you can manipulate the object itself, not just its
    # value.

    my_list = [1, 2]
    test(3)
    test(4, my_list)
    print(my_list)
    test(5)

if __name__ == "__main__":
    main()
