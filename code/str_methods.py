# capitalize() - Return a copy of the string with its first character capitalized and the rest lowercased.
name = "artorias"
print(name.capitalize())

# casefold() - Return a casefolded copy of the string. Casefolded strings may be used for caseless matching. For example it converts German lowercase letter B is equivalent to "ss".
boss = "Calameet"
print(boss.casefold())

# center(width, [, fillchar]) - Returns centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
# It starts putting the character on the right first if length is one character more than the original string.
lord = "Godfrey"
print(lord.center(len(lord) + 4, "-"))

# count(sub[, start[, end]]) - Returns the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
# If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.
name = "Gideon Offnir"
print(name.count(""))
print(len(name))

# encode(encoding="utf-8", errors="strict") - Returns the string encoded in bytes. errors controls how encoding errors are handled. If "strict" (the default), a UnicodeError exception is raised.
name = "Can"
print(name.encode())

# endswith(suffix[, start[, end]]) - Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optonal end, stop comparing at that position.
some_name = "Jonathan"
print(some_name.endswith("nathan"))
print(some_name.endswith("nathan", 0, 2))

# expandtabs(tabsize=8) - Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Any other character is copied unchanged. It actually insert one or more spaces instead of tab characters.
name = "Can\tKocak"
print(name.expandtabs(10))
print(name.expandtabs(16))

# find(sub[, start[, end]]) - Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted in slice notation. Return -1 if sub is not found.
# The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator.
name = "Jonathan"
print(name.find("athan"))
print("athan" in name)

# format(*args, **kwargs) - Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with string value of the corresponding argument.
print("The sum of 1 + 2 is {}".format(1 + 2))


# format_map(mapping, /) - Forward slash here indicates that mapping parameter should be passed as positional argument only. Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. This is useful if for example mapping is a dict subclass.
class Default(dict):
    def __missing__(self, key):
        return key


print("{name} was born in {country}".format_map(Default(name="Can", country="Turkey")))

# index(sub[, start[, end]]) - Like find(), but raise ValueError when the substring is not found.
name = "Seyfi"
try:
    name.index("e")
except ValueError as e:
    raise e

# isalnum() - Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
name = "Deckard Cain"
print(name.isalnum())

# isalpha() - Return True if all characters in the string are alphabetic and there is at least one character, False otherwise. Alphabetic characters are those characters defined in the Unicode character database as "Letter".
name = "Lilith"
print(name.isalpha())

# isascii() - Return True if the string is empty or all characters in the string are ASCII, False otherwise.
rapper = "Tupac Shakur"
mumble_rapper = ""
print(rapper.isascii())
print(mumble_rapper.isascii())

# isdecimal() - Return True if all characters in the string are decimal characters and there is at least one character, False otherwise. Decimal characters are those that can be used to form numbers in base 10.
number = "1234567890"
print(number.isdecimal())

# isdigit() - Return True if all characters in the string are digits and there is at least one character, False otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits.
birth_year = "1997"
print(birth_year.isdigit())

# isidentifier() - Return True if the string is a valid identifier according to the language definition.
print("Is it true: def".isidentifier())

# islower() - Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.
name = "can"
print(name.islower())

# isnumeric() - Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise.
current_year = "2024"
print(current_year.isnumeric())

# isprintable() - Return True if all characters in the string are printable or the string is empty, False otherwise. Nonprintable characters are those characters defined in the Unicode database as "Other" or "Seperator", except ASCII space (0x20).
name = "Can"
print(name.isprintable())

# isspace() - Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.
spaces = "   "
print(spaces.isspace())

# istitle() - Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
song = "Rock and Stone"
other_song = "The Pursuit Of Vikings"
print(song.istitle())
print(other_song.istitle())

# isupper() - Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
state = "IN_COMBAT"
print(state.isupper())

# join(iterable) - Return a string which is the concatenation of the string in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The seperator between elements is the string providing this method.
cpu = "-".join("Can")
print(cpu)

# ljust(width[, fillchar]) - Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
name = "Can"
print(name.ljust(10, "x"))

# lower() - Return a copy of the string with all cased characters converted to lowercase.
status = "ALIVE"
print(status.lower())

# lstrip([chars]) - Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:
print("www.example.com".lstrip("cmowz"))

# If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.
print("TestHook".removeprefix("Test"))
print("BaseTestCase".removeprefix("Test"))

# removesuffix(suffix, /) - If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.
print("MiscTests".removesuffix("Tests"))
print("TmpDirMixin".removesuffix("Tests"))

# replace(old, new, count=-1) - Return a copy of the string with all occurrences of substring old replaced by new. If count is given, only the first count occurrences are replaced. If count is not specified or -1, then all occurrences are replaced.
name = "Linird Skinird"
print(name.replace("i", "y"))
print(name.replace("i", "y", 2))

# rfind(sub[, start[, end]]) - Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
name = "Mert Caner Can"
print(name.rfind("Can"))
print(name.find("Can"))

# rindex(sub[, start[, end]]) - Like rfind() but raises ValueError when the substring is not found.
name = "Jean Jacque Rosseau"
print(name.rindex("acque"))

# rjust(width[, fillchar]) - Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
name = "Can"
print(name.rjust(11, "#"))
print(name.rjust(11))

# rsplit(sep=None, maxsplit=-1) - Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a seperator. Except for splitting from the right, behaves like split().
name = "Artorias"
print(name.rsplit("r"))

# rstrip([chars]) - Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
print("     spacious        ".rstrip())
print("mississippi".rstrip("ipz"))

# removesuffix() will remove a single suffix string rather than all of a set of characters.
print("Monty Python".rstrip(" Python"))
print("Monty Python".removesuffix(" Python"))

# split(sep=None, maxsplit=-1) - Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have the at most maxsplit + 1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, "1, 2".split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters as single delimiter.
print("1,2,3".split(","))
print("1,2,3".split(",", 1))
print("1,2,,3,".split(","))
print("1<>2<>3<4".split("<>"))
print("1 2 3".split())
print("1 2 3".split(maxsplit=1))
print(" 1   2   3   ".split())

# splitlines(keepends=False) - Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
print("ab c\n\nde fg\rkl\r\n".splitlines())
print("ab c\n\nde fg\rkl\r\n".splitlines(keepends=True))

# startswith(prefix[, start[, end]]) - Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
name = "Caner"
print(name.startswith("Can"))

# strip([chars]) - Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars arguments is not a prefix or suffix; rather, all combinations of its values are stripped:
print("     spacious        ".strip())
print("www.example.com".strip("cmowz"))

comment_string = "#...... Section 3.2.1 Issue #32 ......"
print(comment_string.strip(".#! "))

# swapcase() - Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that s.swapcase().swapcase() == s.
name = "Can"
print(name.swapcase().swapcase())

# title() - Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
song = "the breed of durin"
print(song.title())

# upper() - Return a copy of the string with all the cased characters converted to uppercase. Note that s.upper().isupper() might be False.
name = "can"
print(name.upper())

# zfill(width) - Return a copy of the string left filled with ASCII '0' digits to make a string of length width. A leading sign prefix ('+', '-') is handled by inserting hte padding after the sign character rather than before. The original string is returned if width is less than or equal to len(s).
print("42".zfill(5))
print("-42".zfill(5))
