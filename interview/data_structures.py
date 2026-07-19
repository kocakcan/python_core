import timeit

# Trade-offs first, timing second. The four built-in containers differ on
# three axes: mutability, ordering, and whether elements need to be
# hashable.
#
# - list:  mutable, ordered, elements can be anything (no hashability
#          requirement). Good default "sequence of things" container.
# - tuple: immutable, ordered, elements can be anything -- but the tuple
#          itself is only hashable (usable as a dict key / set member) if
#          every element in it is hashable. Used for fixed-shape records
#          and as dict keys/set members when a list wouldn't be allowed.
# - dict:  mutable, insertion-ordered (guaranteed since 3.7), keys must be
#          hashable (which is why keys are usually str/int/tuple, never
#          list). O(1) average lookup by key via hashing.
# - set:   mutable, unordered, elements must be hashable for the same
#          reason dict keys must be -- a set is really "a dict with no
#          values," backed by the same hash table.
print(f"tuple (1, [2, 3]) hashable? ", end="")
try:
    hash((1, [2, 3]))
    print("yes")
except TypeError as e:
    print(f"no -- {e}")

print(f"tuple (1, 2, 3) hashable? ", end="")
try:
    hash((1, 2, 3))
    print("yes")
except TypeError as e:
    print(f"no -- {e}")

print("---")


# Big-O of common operations, demonstrated rather than just asserted:
#   list:  index/append/pop-from-end -> O(1); insert(0)/pop(0) -> O(n)
#          (every remaining element has to shift); `in` -> O(n) (linear scan)
#   dict/set: `in`, get, add -> O(1) average (hash lookup, not a scan)
#
# The classic interview-relevant one: use a set/dict for membership checks
# on anything you'll query more than once -- a list scan is fine for a
# handful of items but falls over as the collection grows.
N = 50_000
big_list = list(range(N))
big_set = set(big_list)
target = -1  # guaranteed absent -- worst case for a linear scan, no early exit

list_time = timeit.timeit(lambda: target in big_list, number=200)
set_time = timeit.timeit(lambda: target in big_set, number=200)
print(f"'in' on a {N}-element list, 200 lookups: {list_time:.4f}s")
print(f"'in' on a {N}-element set,  200 lookups: {set_time:.4f}s")
print(f"set was ~{list_time / set_time:.0f}x faster -- O(1) hash lookup vs O(n) scan")

print("---")


small_list = list(range(5_000))


def append_then_pop():
    small_list.append(0)
    small_list.pop()


def insert_then_pop():
    small_list.insert(0, 0)
    small_list.pop(0)


append_time = timeit.timeit(append_then_pop, number=20_000)
insert_time = timeit.timeit(insert_then_pop, number=20_000)
print(f"append+pop (end),   20k ops: {append_time:.4f}s")
print(f"insert+pop (front), 20k ops: {insert_time:.4f}s")
print("insert(0)/pop(0) are slower -- every other element shifts by one index;")
print("append()/pop() at the end don't disturb anything else, so they're O(1)")
print("(use collections.deque instead of a list if you need fast operations at both ends)")
