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

# insert(i, x) - Insert an item at a given position.
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x)
# is equivalent to a.append(x)
bosses = ["General Radahn", "Knight Artorias", "Pontiff Sulyvahn"]
print(bosses)
bosses.insert(0, "Gwyn")
print(bosses)
bosses.insert(len(bosses), "Lady Maria")
print(bosses)

# remove(x) - Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
try:
    bosses.remove("Gwyn")
    print(bosses)
except ValueError:
    print("Specified boss is not present in the list.")

# pop(i) - Remove the item at the given position in the list, returning it.
# If no index is specified, a.pop() removes and returns the last item in
# the list. It raises and IndexError if the list is empty or the index is
# outside the list range.
try:
    fav_boss = bosses.pop(1)
    print(f"{fav_boss} is my favourite boss in souls series.")
except IndexError:
    print("There is no such boss in the list.")

# clear() - Remove all items from the list. Equivalent to del a[:].
bosses.clear()
print(bosses)

# index(x, [, start[, end]]) - Return zero-based index in the list of the
# first item whose value is equal to x. Raises a ValueError if there is no
# such item. The optional arguments start and end are interpreted as in the
# slice notation and are used to limit the search to a particular subsequence
# of the list. The returned index is computed relative to the beginning of the
# full sequence rather than the start argument.
fruits = ["orange", "apple", "pear", "banana", "kiwi"]
print(fruits)
try:
    fruits.insert(fruits.index("banana"), "watermelon")
    print(fruits)
except ValueError:
    print("Banana is not in the list mate.")

# count(x) - Return the number of times x appears in the list.
import random
numbers = [random.randint(0, 30) for i in range(0, 30)]
print(numbers)
number = int(input("Provide an integer to find its occurrence: "))
print(f"There are total of {numbers.count(number)} {number}.")

# sort(*, key=None, reverse=False) - Sort the items of the list in place
numbers.sort()
print(numbers)

# reverse() - Reverse the elements of the list in place.
numbers.reverse()
print(numbers)

# copy() - Return a shallow copy of the list.
# Equivalent to a[:].
nums = numbers.copy()
print(nums)

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
print(fruits.index("banana"))
fruits.reverse()
print(fruits)
fruits.append("grape")
print(fruits)
fruits.sort()
print(fruits)
