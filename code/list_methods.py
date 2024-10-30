# append(x) - Add an item to the end of the list.
# Equivalent to a[len(a):] = [x] or a[len(a):len(a)] = [x]
scores = [19, 50, 30]
print(scores)
scores.append(100)
print(scores)

# extend(iterable) - Extend the list by appending all the items from
# the iterable. Equivalent to a[len(a):] = iterable
odd_numbers = [i for i in range(1, 30) if not i % 2]
even_numbers = [i for i in range(1, 30) if i % 2]
print(odd_numbers)
print(even_numbers)
odd_numbers.extend(even_numbers)
odd_numbers.sort()
print(odd_numbers)
