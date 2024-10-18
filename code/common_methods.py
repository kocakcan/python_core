# Common Sequence Operations
s = "Rammstein"
x = "stein"
y = "Can"

print(x in s)
print(y not in s)

# Concatenation
print(y + x)

# Repetition
print(y * 5)

# Subscripting
print(y[0])

# Slicing
print(s[:-1])   # Rammstei

# len
print(len(s))

# min - Smallest item
print(min(s))

# max - Largest item
print(max(s))

# s.index(x[, i[, j]]) - index of the first occurrence of x in s
# at or after index i and before index j
print(s.index('s'))

# s.count(x) - total number of occurrences of x in s
print(s.count('s'))
