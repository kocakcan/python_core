import sys

# Iterable: has __iter__, can be looped over
my_list = [1, 2, 3]

# Iterator: has __iter__ and __next__, remembers state
my_iterator = iter(my_list)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))    # raises exception
try:
    print(next(my_iterator))
except StopIteration as e:
    raise e

def counter(limit):
    print("Starting!")
    n = 0
    while n < limit:
        yield n
        print(f"Resumed after yielding {n}")
        n += 1

gen = counter(3)
print("Generator created, nothing printed yet? Let's see...")
print(next(gen))
print(next(gen))
print(next(gen))

# List comprehension builds everything in memory immediately
list_comp = [x**2 for x in range(1_000_000)]

# Generator expression builds nothing yet, just a recipe
gen_comp = (x**2 for x in range(1_000_000))
print(sys.getsizeof(list_comp))
print(sys.getsizeof(gen_comp))

gen = (x for x in range(3))
print(list(gen))
print(list(gen))

def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))
# print(next(g))    # raises StopIteration

g = gen()
while True:
    try:
        value = next(g)
        print(value)
    except StopIteration:
        break

def gen_2():
    yield 1
    yield 2
    # return value in a generator becomes StopIteration's value, NOT a yielded
    # value
    return "done"

g = gen_2()
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration as e:
    print(e.value)

def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))

def chunked(iterable, size):
    bucket = []
    for item in iterable:
        bucket.append(item)
        if len(bucket) == size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket

print(list(chunked([1, 2, 3, 4, 5, 6, 7], 3)))
