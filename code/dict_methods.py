"""
Below are the operations that dictionaries support (and therefore, custom
mapping types should support too):
"""

# list(d) - Return a list of all the keys used in the dictionary d.
my_d = {x: x ** 2 for x in range(100)}
print(list(my_d))

# this does not work as the keys are not hashable
# another_d = {
#     [0, 1, 2]: "first",
#     [3, 4, 5]: "second",
# }

# len(d) - Return the number of items in the dictionary d.
print(f"There are {len(my_d)} items in my_d.")

"""
    d[key]
    Return the item of d with key key. Raises a KeyError if key is not in the
    map.

    - If a subclass of dict defines a method __missing__() and key is not
    present, the d[key] operation calls that method with the key key as
    argument. 
    - The d[key] operation then returns or raises whatever is returned
    or raised by the __missing__(key) call. 
    - No other operations or methods invoke __missing__(). If __missing__() is not defined, KeyError is raised.
    - __missing__() must be a method; it cannot be an instance variable:
"""
class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()
print(c["red"])
c["red"] += 1
print(c["red"])
"""
    d[key] = value
    Set d[key] to value.
"""
http_request = {
    "url": "https://www.google.com",
    "Content-Type": "application/json",
    "auth": "feqnj42314k12lo",
}

print(f"Content-Type is {http_request['Content-Type']}")
http_request["Content-Type"] = "text/html"
print(f"Content-Type is {http_request['Content-Type']}")

"""
    del d[key]
    Remove d[key] from d. Raises a KeyError if key is not in the map.
"""
try:
    del http_request["some_header"]
except KeyError:
    print("It does not exist mate.")

"""
    key in d
    Return True if d has a key key, else False.
"""
print("auth" in http_request)

"""
    key not in d
    Equivalent to not key in d.
"""
print("guts" not in http_request)
print(not "guts" in http_request)

"""
    iter(d)
    Return an iterator over the keys of the dictionary. This is a shortcut for
    iter(d.keys())
"""
print(list(iter(http_request)))

"""
    clear()
    Remove all items from the dictionary.
"""
http_request.clear()
print(http_request)

"""
    copy()
    Return a shallow copy of the dictionary.
"""
request = http_request.copy()
print(request)

"""
    get(key, default=None)
    Return the value for key if key is in the dictionary, else default. If
    default is not given, it defaults to None, so that this method never raises a
    KeyError.
"""
player = {
    "name": "Can",
    "level": 237,
    "attack": 25034,
    "armor": 138,
    "life": 9238,
}

print(player.get("name"))
print(player.get("paragon_level", "You haven't specified it"))

"""
    items(d)
    Return a new view of the dictionary's items ((key, value) pairs).
"""
for i, j in player.items():
    print(i, j)

"""
    keys()
    Return a new view of the dictionary's keys.
"""
for key in player.keys():
    print(key)

"""
    pop(key[, default])
    If key is in the dictionary, remove it and return its value, else return
    default. If default is not given and key is not in the dictionary, a
    KeyError is raised.
"""
try:
    life_rating = player.pop("life")
except KeyError:
    print("No default value and key isn't present in the dict.")

"""
    popitem()
    Remove and return a (key, value) pair from the dictionary. Pairs are
returned in LIFO order.
    If the dictionary is empty, calling popitem() raises a KeyError.
"""
try:
    key, value = player.popitem()
    print(key, value)
except KeyError:
    print("dict is empty")

"""
    reversed(d)
    Return a reverse iterator over the keys of the dictionary. This is a
    shortcut for reversed(d.keys())
"""
for key in reversed(player):
    print(key)

"""
    setdefault(key, default=None)
    If key is in the dictionary, return its value. If not, insert key with a
    value of default and return default. default defaults to None.
"""
print(player.setdefault("paragon_level", 237))

"""
    update([other])
    Update the dictionary with the key/value pairs from other, overwriting
    existing keys. Return None.

    update() accepts either another object with a keys() method or an iterable
    of key/value pairs (as tuples or other iterables of length two.). If
    keyword arguments are specified, the dictionary is then updated with those
    key/value pairs: d.update(red=1, blue=2)
"""
player.update(clan="Groots")
print(player)

"""
    values()
    Return a new view of the dictionary's values.

    An equality comparison between one dict.values() view and another will
    always return False. This also applies when comparing dict.values() to
    itself.
"""
d = {'a': 1}
print(d.values() == d.values())

"""
    d | other
    Create a new dictionary with the merged keys and values of d and other,
    which must both be dictionaries. The values of other take priorit when d
    and other share keys.
"""
d2 = {'b': 2}
print(d | d2)

"""
    d |= other
    Update the dictionary d with keys and values from other, which may be
    either a mapping or an iterable of key/value pairs. The values of other
    take priority when d and other share keys.
"""

# Dictionaries compare equal if and only if they have same (key, value) pairs
# (regardless of ordering). Order comparisons ('<', '<=', '>', '>=') raises
# TypeError.

# Dictionaries preserve insertion order. Note that updating a key does not
# affect the order. Keys added after deletion are inserted at the end.
d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d)
print(list(d))
print(list(d.values()))
d["one"] = 42
print(d)
del d["two"]
d["two"] = None
print(d)
