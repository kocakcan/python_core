# functools - Higher-order functions and operations on callable objects
# The functools module is for higher-order functions: functions that act on or
# return other functions. In general, any callable object can be treated as a
# function for the purposes of this module.

import statistics
from functools import cache, cached_property, lru_cache, partialmethod, singledispatch, singledispatchmethod, total_ordering, partial

"""
    @functools.cache(user_function)

    - Caches a function's computed results for given input arguments, allowing
      subsequent calls with the same arguments to return the cached result
      instead of recomputing it, thus improving performance for functions with
      expensive computation or frequent calls.
    - Also known as lru_cache() and "memoize".
"""

"""
    @functools.cached_property(func)

    - Converts a method into a property whose value is computed once and
      cached, allowing subsequent access to return the cached value instead of
      recalculating it, which can enhance performance for expensive
      calculations in class instances.
"""

"""
    functools.cmp_to_key(func)

    - Transforms an old-style comparison function (using cmp()) into a key
      function for sorting operations, enabling the use of richer comparison
      logic in sorting functions like sorted() without requiring the
      traditional comparison signature.
"""

"""
    @functools.lru_cache(user_function)
    @functools.lru_cache(maxsize=128, typed=False)

    - Caches the results of a function call, allowing it to efficiently store
      and retrieve previously computed values based on input arguments, while
      limiting the cache size using a least-recently-used (LRU) eviction policy
      to manage memory usage efficiently.
"""

"""
    @functools.total_ordering

    - Simplifies the implementation of rich comparison methods in a class by
      requiring only one or more of the basic comparison methods (like __lt__,
      __le__, __gt__, __ge__) to be defined, automatically generating the
      others to create a complete set of rich comparison operations.
"""

"""
    @functools.partial(func, /, *args, **keywords)

    - Creates a new function by fixing a specified number of arguments of an
      existing function, allowing you to call the new function with fewer
      arguments, effectively pre-setting some values for later use.
"""

"""
    class functools.partialmethod(func, /, *args, **keywords)

    - Allows you to create a method in a class that has some of its arguments
      pre-filled, enabling instance of the class to call the method with fewer
      arguments while maintaining the flexibility of using the full method
      signature when needed.
"""

"""
    @functools.singledispatch

    - Transforms a function into a generic function that can register different
      implementations based on the type of the first argument, allowing for
      type-specifi behaviour using a single interface, thereby enabling
      polymorphic funciton dispatching without the use of multiple overloads.
"""

"""
    class functools.singledispatchmethod(func)

    - Creates a generic method that can register different implementations
      based on the type of its first argument, allowing class methods to behave
      polymorphically according to the type of the first argument while
      maintaining the traditional method binding.
"""

"""
    functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES)

    - 
"""

# class Negator:
#     @singledispatchmethod
#     def neg(self, arg):
#         raise NotImplementedError("Cannot negate a")
#
#     @neg.register
#     def _(self, arg: int):
#         return -arg
#
#     @neg.register
#     def _(self, arg: bool):
#         return not arg

# @singledispatchmethod supports nesting with other decorators such as
# @classmethod. Note that to allow for dispatcher.register,
# singledispatchmethod must be the outer most decorator. Here is the Negator
# class with the neg methods bound to the class, rather than an instance of the
# class:
class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in number, eh?", end= " ")
    print(arg)

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

# types.UnionType and typing.Union can also be used:
# @fun.register
# def _(arg: int | float, verbose=False):
#     if verbose:
#         print("Strength in numbers, eh?", end=" ")
#     print(arg)

# from typing import Union
# @fun.register
# def _(arg: Union[list, set], verbose=False):
#     if verbose:
#         print("Enumerate this:")
#     for i, elem in enumerate(arg):
#         print(i, elem)

# For code which doesn't use type annotations, the appropriate type argument
# can be passed explicitly to the decorator itself:
@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg)

# For code that dispatches on a collections type (e.g., list), but wants to
# typehint the items of the collection (e.g., list[int]), the dispatch type
# should be passed explicitly to the decorator itself with the typehint going
# in to the function definition:
@fun.register(list)
def _(arg: list[int], verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

# To enable registering lambdas and pre-existing functions, the register()
# attribute can also be used in a functional form:
def nothing(arg, verbose=False):
    print("Nothing.")

class Cell:
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)
        
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

# Partial is roughly equivalent to:
# def partial(func, /, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):
#         newkeywords = {**keywords, **fkeywords}
#         return func(*args, *fargs, **newkeywords)
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc

# @total_ordering
# class Student:
#     def _is_valid_operand(self, other):
#         return (hasattr(other, "lastname") and
#                 hasattr(other, "firstname"))
#
#     def __eq__(self, other):
#         if not self._is_valid_operand(other):
#             return NotImplemented
#         return ((self.lastname.lower(), self.firstname.lower()) ==
#                 (other.lastname.lower(), self.firstname.lower()))
#
#     def __lt__(self, other):
#         if not self._is_valid_operand(other):
#             return NotImplemented
#         return ((self.lastname.lower(), self.firstname.lower()) ==
#                 (other.lastname.lower(), self.firstname.lower()))


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in "AEIOUaeiou")

class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)

@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1

def main():
    # no previously cached result, makes 11 recursive calls
    print(factorial(10))

    # just looks up cached value result
    print(factorial(5))

    # makes two new recursive calls, the other 10 are cached
    print(factorial(12))

    dataset = DataSet(list(range(1, 101)))
    # stdev is computed only once, any subsequent calls after this will return
    # the cached result
    print(dataset.stdev)

    print(count_vowels("Peter Piper picked a peck of pickled Peppers:"
"Did Peter Piper pick a peck of pickled Peppers?"))

    # Generating Fibonnacci numbers using cache
    print([fib(n) for n in range(16)])
    print(fib.cache_info())

    basetwo = partial(int, base=2)
    basetwo.__doc__ = "Convert base 2 string to an int."
    print(basetwo("10010"))

    c = Cell()
    print(c.alive)

    c.set_alive()
    print(c.alive)

    # Can still use set_state
    c.set_state(False)
    print(c.alive)
    

    # The register() attribute returns the undecorated function.
    # This enables decorator stacking, pickling, and the creation of unit tests
    # for each variant independently.
    fun.register(type(None), nothing)

    # When called, the generic function dispatches on the type of the first
    # argument:
    fun("Hello, world.")
    fun("test.", verbose=True)
    fun(42, verbose=True)
    fun(["spam", "spam", "eggs", "spam"], verbose=True)
    fun(None)
    fun(1.23)

    # When there is no registered implementation for a specific type, its
    # method resolution order is used to find a more generic implementation.
    # The original function decorated with @singledispatch is registered for
    # the base object type, which means it is used if no better implementation
    # is found.

    # If an implementation is registered to an abstact base class, virtual
    # subclasses of the base class will be dispatched to that implementation:
    from collections.abc import Mapping
    @fun.register
    def _(arg: Mapping, verbose=False):
        if verbose:
            print("Keys & Values")
        for key, value in arg.items():
            print(key, "=>", value)

    fun({'a': 'b'})

    # To check which implementation the generic function will choose for a
    # given type, use the dispatch() attribute:
    fun.dispatch(float)

    # To access all registered implementations, use the read-only registry
    # attribute:
    print(fun.registry.keys())

    n = False

    print(n)

    n = Negator.neg(n)
    print(n)

if __name__ == "__main__":
    main()
