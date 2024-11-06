# len(s) - Return the number of elements in set s (cardinality of s).
s1 = {c for c in "abracadabra" if c not in "abc"}
print(s1)
print(len(s1))

# x in s - Text x for membership in s.
print('z' in s1)

# x not in s - Test x for non-membership in s.
print('x' in s1)

# isdisjoint(other) - Return True if the set has no elements in common with
# other. Sets are disjoint if and only if their intersection is the empty set.
s2 = {"Sets are super useful"}
print(s2)
if s1.isdisjoint(s2):
    print("They are disjoint sets, " 
    "meaning their intersection is the empty set.")

# issubset(other)
# set <= other - Test whether every element in the set is in other.
s1 = {1, 3, 5}
s2 = {1, 3, 5, 7}
print("s1 is subset of s2:", s1.issubset(s2))

# set < other - Test whether the set is a proper subset of other, that is, set <=
# other and set != other.
print("s1 is proper subset of s2:", s1 < s2)

# issuperset(other)
# set >= other - Test whether every element in other is in the set.
print("s2 is superset of s1:", s2.issuperset(s1))

# set > other - Test whether the set is a proper superset of other, set >=
# other and set != other.
print("s2 is proper superset of s1:", s2 > s1)

# union(*others)
# set | other | ... - Return a new set with elements from the set and all
# others.
s1 = {c for c in "Can" if c in "aeiou"}
s2 = {c for c in "Medet" if c in "aeiou"}
s3 = {c for c in "Seyfi" if c in "aeiou"}
s4 = {c for c in "Leyli" if c in "aeiou"}
s5 = {c for c in "Dilan" if c in "aeiou"}
print(s1.union(s2, s3, s4, s5))

# intersection(*others)
# set & other & ... - Return a new set with elements common to the set and all
# others.
print(s1.intersection(s2, s3, s4, s5))

# difference(*others)
# set - other - ... - Return a new set with elements in the set that are not in
# the others.
print(s1.difference(s2, s3, s4, s5))

# symmetric_difference(other)
# set ^ other - Return a new set with elements in either the set or other but
# not both.
print(s1.symmetric_difference(s2))

# copy() - Return a shallow copy of the set.
s2 = s1.copy()
print(s2)

# update(*others)
# set |= other | ... - Update the set, keeping only elements found in it and
# all others.
s1 = {c for c in "abracadabra"}
s2 = {c for c in "houdini"}
s1.update(s2)
print(s1)

# intersection_update(*others)
# set &= other & ... - Update the set, removing elements found in others.
s1.intersection_update(s2)
print(s1)

# difference_update(*others)
# set -= other | ... - Update the set, removin elements found in others.
s1.difference_update(s2)
print(s1)

# symmetric_difference_update(other)
# set ^= other - Update the set, keeping only elements found in either set, but
# not in both.
s1.symmetric_difference(s2)
print(s1)

# add(elem) - Add element elem to the set.
s1 = {c for c in "Can"}
s1.add('m')
print(s1)

# remove(elem) - Remove element elem from the set. Raises KeyError if elem is
# not contained in the set.
try:
    s1.remove('a')
except KeyError:
    print("It's not in the set.")

# discard(elem) - Remove element elem from the set if it is present.
s1.discard('c')
print(s1)

# pop() - Remove and return an arbitrary element from the set. Raises KeyError
# if the set is empty.
try:
    s1.pop()
except KeyError:
    print("It's not in the set.")

# clear() - Remove all elements in the set.
s1.clear()
print(s1)
