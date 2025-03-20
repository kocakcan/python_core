# itertools - Functions creating iterators for efficient looping
# This module implements a number of iterator building blocks

# The following functions all construct and return iterators. Some provide
# streams of infinite infinite length, so they should only be accessed by
# functions or loops that truncate the stream.

import operator
from itertools import accumulate, compress, dropwhile, filterfalse, groupby, permutations, product, repeat, islice, chain, combinations, count, pairwise, takewhile, zip_longest

"""
    itertools.accumulate(iterable[, function, *, initial=None])

    - Returns an iterator that generates accumulated sums or results from an
      iterable, applying a specified binary function (by default, addition) to
      the elements of the iterable in a cumulative manner, producing an
      intermediate result for each step.
"""

# Roughly equivalent to:
def accumulate_(iterable, function=operator.add, *, initial=None):
    "Return running totals"
    # accumulate([1, 2, 3, 4, 5]) -> 1 3 6 10 15
    # accumulate([1, 2, 3, 4, 5], initial=100) -> 100 101 103 106 110 115
    # accumulate([1, 2, 3, 4, 5], operator.mul) -> 1 2 6 24 120

    iterator = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(iterator)
        except StopIteration:
            return

    yield total
    for element in iterator:
        total = function(total, element)
        yield total

"""
    itertools.batched(iterable, n, *, strict=False)

    - Creates an iterable that groups elements from an input iterable into
      fixed-size batches, returning each batch as a list, which simplifies the
      process of processing or consuming elements in chunks of a specified
      size.
    - The last batch may be shorter than n.
    - If strict is true, will raise a ValueError if the final batch is shorter
      than n.
"""

# Roughly equivalent to:
def batched(iterable, n, *, strict=False):
    # batched("ABCDEFG", 3) -> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")

    iterator = iter(iterable)
    
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError("batched(): incomplete batch")
        yield batch

"""
    itertools.chain(*iterables)

    - Make an iterator that returns elements from the first iterable until it
      is exhausted, then proceeds to the next iterable, until all of the
      iterables are exhausted. This combines multiple data sources into a
      single iterator.
"""

# Roughly equivalent to:
def chain_(*iterables):
    # chain("ABC", "DEF") -> A B C D E F
    for iterable in iterables:
        yield from iterable

"""
    classmethod chain.from_iterable(iterable)

    - Alternate constructor for chain().
    - Gets chained inputs from a single iterable argument that is evaluated
      lazily.
"""

# Roughly equivalent to:
def from_iterable(iterables):
    # chain.from_iterable(["ABC", "DEF"]) -> A B C D E F
    for iterable in iterables:
        yield from iterable

"""
    itertools.combinations(iterable, r)

    - Returns an iterator of tuples containing all possible combinations of a
      specified length from the input variable, generating each combination in
      lexicographical order without repetition, making it useful for scenarios
      where the order of selection does not matter.
"""

# Roughly equivalent to:
def combinations_(iterable, r):
    # combinations("ABCD", 2) -> AB AC AD BC BD CD
    # combinations(range(4), 3) -> 012 013 023 123

    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return
    
    indices = list(range(r))

    yield tuple(pool[i] for i in indices)
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        
        indices[i] += 1

        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        yield tuple(pool[i] for i in indices)

"""
    itertools.combinations_with_replacement(iterable, r)

    - Returns an iterator of tuples containing all possible combinations of a
      specified length from the input variable, allowing for repeated elements,
      and generating each combination in lexicographical order, where the same
      element can appear multiple times in a combination.
"""

# Roughly equivalent to:
def combinations_with_replacement_(iterable, r):
    # combinations_with_replacement("ABC", 2) -> AA AB AC BB BC CC
    
    pool = tuple(iterable)
    n = len(pool)

    if not n and r:
        return

    indices = [0] * r

    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

"""
    itertools.compress(data, selectors)

    - Takes two iterables as input and returns an iterator that yields elements
      from the first iterable only when the corresponding element in the second
      iterable is True, effectively filtering the first iterable based on the
      truth values of the second iterable.
"""

# Roughly equivalent to:
def compress_(data, selectors):
    # compress("ABCDEF", [1, 0, 1, 0, 1, 1]) -> A C E F
    return (datum for datum, selector in zip(data, selectors) if selector)

"""
    itertools.count(start=0, step=1)

    - Make an iterator that returns evenly spaced values beginning with start.
    - Can be used with map() to generate consecutive data points or with zip()
      to add sequence numbers.
"""

# Roughly equivalent to:
def count_(start=0, step=1):
    # count(10) -> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

"""
    itertools.cycle(iterable)

    - Returns an iterator that repeatedly cycles through the elements of an
      input iterable, generating an endless sequence of its elements, making it
      useful for scenarios where you want to loop through a list indefinitely.
"""

# Roughly equivalent to:
def cycle_(iterable):
    # cycle("ABCD") -> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element

"""
    itertools.dropwhile(predicate, iterable)

    - Returns an iterator that skips elements from the input iterable as long
      as a specified predicate function returns true; once the predicate
      returns false, it yields all subsequent elements, including the first
      element that caused the predicate to return false.
"""

# Roughly equivalent to:
def dropwhile_(predicate, iterable):
    # dropwhile(lambda x: x < 5, [1, 4, 6, 3, 8]) -> 6 3 8

    iterator = iter(iterable)
    for x in iterator:
        if not predicate(x):
            yield x
            break

    for x in iterator:
        yield x

"""
    itertools.filterfalse(predicate, iterable)

    - Returns an iterator that filters elements from the input iterable,
      yielding only those for which the specified predicate function returns
      fase, effectively creating an iterator of elements that do not satisfy
      the condition defined by the predicate.
"""

# Roughly equivalent to:
def filterfalse_(predicate, iterable):
    # filterfalse(lambda x: x < 5, [1, 4, 6, 3, 8]) -> 6 8
    
    if predicate is None:
        predicate = bool

    for x in iterable:
        if not predicate(x):
            yield x

"""
    itertools.groupby(iterable, key=None)

    - Make an iterator that returns consecutive keys and groups from the
      iterable.
    - The key is a function computing a key value for each element. If not
      specified or is None, key defaults to an identity function and returns
      the element unchanged.
    - Generally, the iterable needs to already be sorted on the same key
      function.
"""

"""
    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, end])

    - Returns an iterator that slices the input iterable, allowing you to
      specify a start, stop, and optional step, effectively generating a
      sub-iterator that contains only the specified range of elements from the
      original iterable.
"""

"""
    itertools.pairwise(iterable)

    - Return successive overlapping pairs taken from the input variable.
"""

# Roughly equivalent to:
def pairwise_(iterable):
    # pairwise("ABCDEFG") -> AB BC CD DE EF FG
    
    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b

"""
    itertools.permutations(iterable, r=None)

    - Return successive r length permutations of elements from the iterable.
    - If r is not specified or is None, then r defaults to the length of the
      iterable and all possible full-length permutations are generated.
"""

"""
    itertools.product(*iterables, repeat=1)

    - Cartesian product of the input iterables.
    - Roughly equivalent to nested for-loops in a generator expression.
"""

"""
    itertools.repeat(object, [, times])

    - Make an iterator that returns object over and over again.
    - Runs indefinitely unless the times argument is specified.
"""

"""
    itertools.starmap(function, iterable)

    - Make an iterator that computes the function using arguments obtained from
      the iterable.
"""

"""
    itertools.takewhile(predicate, iterable)

    - Make an iterator that returns elements from the iterable as long as the
      predicate is true.
"""

# Roughly equivalent to:
def takewhile_(predicate, iterable):
    # takewhile(lambda x: x < 5, [1, 4, 6, 3, 8]) -> 1 4
    for x in iterable:
        if not predicate(x):
            break
        yield x

"""
    itertools.tee(iterable, n=2)

    - Return n independent iterators from a single iterable
"""

"""
    itertools.zip_longest(*iterables, fillvalue=None)

    - Make an iterator that aggregates elements from each of the iterables.
    - If the iterables are of uneven length, missing values are filled-in with
      fillvalue. If not specified, fillvalue defaults to None.
"""

def main():
    print(list(accumulate_([1, 2, 3, 4, 5])))

    # To compute a running minimum, set function to min(). For a running maximum,
    # set function to max(). Or for a running product, set function to
    # operator.mul(). To build an amortization table, accumulate the interest and
    # apply payments:

    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    # running maximum
    print(list(accumulate(data, max)))

    # running product
    print(list(accumulate(data, operator.mul)))

    # Amortize a 5% loan of 1000 with 10 annual payments of 90
    update = lambda balance, payment: round(balance * 1.05) - payment
    print(list(accumulate(repeat(90, 10), update, initial=1_000)))

    flattened_data = ["roses", "red", "violets", "blue", "sugar", "sweet"]
    unflattened = list(batched(flattened_data, 2))
    print(unflattened)

    print(list(chain_("ABC", "DEF")))

    print(list(combinations_("ABCD", 2)))
    print(list(combinations("ABCD", 2)))

    print(list(combinations_with_replacement_("ABC", 2)))

    print(list(compress("ABCDEF", [1, 0, 1, 0, 1, 1])))
    print(list(compress_("ABCDEF", [1, 0, 1, 0, 1, 1])))

    print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 3, 8])))

    print(list(filterfalse(lambda x: x < 5, [1, 4, 6, 3, 8])))
    print(list(filterfalse_(lambda x: x < 5, [1, 4, 6, 3, 8])))

    print([k for k, g in groupby("AAAABBBCCDAABBB")])

    print(list(islice("ABCDEFG", 2)))
    print(list(islice("ABCDEFG", 2, 4)))
    print(list(islice("ABCDEFG", 2, None)))
    print(list(islice("ABCDEFG", 0, None, 2)))

    print(list(pairwise("ABCDEFG")))
    print(list(pairwise_("ABCDEFG")))

    print(list(permutations("ABCD", 2)))

    print(list(product("ABCD", "xy")))

    print(list(repeat(10, 3)))

    print(list(takewhile_(lambda x: x < 5, [1, 4, 6, 3, 8])))
    print(list(takewhile(lambda x: x < 5, [1, 4, 6, 3, 8])))

    print(list(zip_longest("ABCD", "xy", fillvalue='-')))

    
if __name__ == "__main__":
    main()
