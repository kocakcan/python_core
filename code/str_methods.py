# Value of n less than 0 are treated as 0
# (which yields an empty sequence of the same type as s)
# Note that items in the sequence s are not copied; they are referenced multiple times.
lists = [[5]] * 3
print(lists)
# What has happened is that [[5]] is a one-element list containing a list with a single element
# so all three elements of [[5]] * 3 are references to this list. Modifying any of the elements
# of lists modifies this single list.
name = "Can"
print(name[-1])
print(name[len(name) -1])
# Concatenating immutable sequences always results in a new object.
# This means that building up a sequence by repeated concatenation will have
# a quadratic runtime cost in the total sequence length.
name = "Can"
surname = "Kocak"
full_name = name.join(surname)
print(full_name)
