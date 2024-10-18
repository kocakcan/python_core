# Mutable Sequence Types
bosses = ["Godfrey", "Hoarah Loux", "Elemer", "Messmer"]

# s[i] = x - item i of s is replaced by x
bosses[-1] = "Malenia"
print(bosses)

# s[i:j] = t - slice of s from i to j is replaced by the contents of the iterable t
bosses[:-2] = ["Gideon Offnir", "General Radahn"]
print(bosses)

# del s[i:j] - same as s[i:j] = []
del bosses[:2]  # same as bosses[0:2]
print(bosses)

# s[i:j:k] = t - the elements of s[i:j:k] are replaced by those of t
bosses[0:2:1] = ["Astel", "Metyr"]
print(bosses)

# del s[i:j:k] - remove elements of s[i:j:k] from the list
del bosses[::]
print(bosses)

# s.append(x) - appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
bosses.append("General Radahn")
print(bosses)

# s.clear() - removes all items from s (same as del s[:] and del s[::])
# bosses.clear()
del bosses[:]
print(bosses)

# s.copy() - creates a shallow copy of s (same as s[:])
other_bosses = bosses.copy()
print(other_bosses)

# s.extend(t) or s += t - extends s with the contents of t
# for the most part the same as s[len(s):len(s)] = t
bosses.extend(["Niall", "Onyx Greatlord"])
print(bosses)

# s *= n - updates s with its contents repeated n times
bosses *= 2
print(bosses)

# s.insert(i, x) - inserts x into s at the index given by i
# same as s[i:i] = [x]
bosses.insert(2, "Radagon")
print(bosses)

# s.pop() or s.pop(i) - retrieves the item at i and also removes it from s
# i defaults to -1, so that by default the last item is removed and returned
fav_boss = bosses.pop(2)
print(fav_boss)
print(bosses)

# s.remove(x) - removes the first item from s where s[i] is equal to x
bosses.remove("Onyx Greatlord")
print(bosses)

# s.reverse() - reverses the items of s in place.
bosses.reverse()
print(bosses)
