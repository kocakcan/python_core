import random


def reverse_order(s):
    s_list = s.split()
    return " ".join(reversed(s_list))


def main():
    # d = {
    #     "name": "Can",
    #     "age": 28,
    #     "is_engineer": True,
    #     "rate": 0.79,
    #     "cv_score": 79,
    #     "hobbies": ["Coding", "Playing video games"],
    # }
    #
    # d2 = dict([(1, "foo"), (10, "bar")])
    # # print(d2)
    #
    # name = d["name"]
    # print(name)
    #
    # try:
    #     print(d["gender"])
    # except KeyError:
    #     print("No key exists named gender")
    #
    # print(d.get("gender", "No key exists named gender"))
    #
    # # Update
    # d["rate"] = 0.91
    # d["hobbies"].append("Playing guitar")
    #
    # print(d["hobbies"])
    # print(d["rate"])
    #
    # # Delete
    # try:
    #     del d["invalid_key"]
    # except KeyError:
    #     print("No such key exists")
    #
    # for _ in d.items():
    #     print(_)
    #
    # for _ in d.values():
    #     print(_)
    #
    # # Membership check
    # if "hobbies" in d and d["is_engineer"]:
    #     print("Both keys exist")
    #
    # # Dictionary keys should be hashable
    # # int, float, string, tuple are all hashable types
    # text = "can kocak"
    # print(text.split(" "))
    #
    # t = "a good     example"
    # print(reverse_order(t))
    boss: str = "arToRIas"
    print(boss.capitalize())

    input, output = "scheiße", "SCHEISSE"
    print(input.casefold() == output.casefold())

    # gen_expr = (x*x for x in range(0, 10))

    next_boss: str = "Ornstein & Smough"
    # Starts putting the character on the right first
    print(next_boss.center(len(next_boss) + 5, "*"))

    print(f"Result of count(): {next_boss.count('')}")
    print(f"Result of len(): {len(next_boss)}")
    print(f"Result of count('Smough') in {next_boss}: {next_boss.count('Smough')}")

    boss_in_bytes = boss.encode()
    print(boss_in_bytes)

    name: str = "can"
    other_name: str = "Mertcan"
    print(other_name.endswith("can"))

    # print(name.expandtabs(10))
    print(f"{name} occurs at index {other_name.find(name)} in {other_name}")
    print(name in other_name)

    print("My name is {}".format(name.capitalize()))

    father_name: str = "Seyfi"
    try:
        father_name.index("l")
    except ValueError as e:
        print(e)
    finally:
        print("we're done here lad")

    print("!@#$%^&*()_+".isalnum())
    print(f"yield is an identifier: {'yield'.isidentifier()}")

    print(father_name.islower())
    print(father_name.isupper())
    print("\t\n".isprintable())

    song: str = "To Be A Dwarf"
    print(song.istitle())

    # print("-".join(father_name))
    text: str = "canhello world"
    print(text.lstrip("can"))

    print("Test Case #100".removeprefix("Test Case"))
    print("Best Test Case".removeprefix("Test Case"))
    print("Best Test Case".removesuffix("Test Case"))

    soundtrack: str = "Break the Rules"
    print(soundtrack.replace("Rules", "Records"))

    print("Alican Caner".casefold().rfind("can"))
    try:
        print("Can Kocak".rindex("Kocek"))
    except ValueError as e:
        print(e)

    print(name.rjust(10, "#"))
    print(name.ljust(10, "#"))

    print("Amon Amarth".rsplit("Amarth"))
    print("Amon Amarth".rstrip("Amarth"))
    print("1,2,,3".split(","))
    print("         here    i    am     ".split())

    nums: list[int] = list(range(0, 10))
    nums.append(11)
    print(nums)

    nums.extend(list(range(11, 20)))
    print(nums)

    bosses: list[str] = ["Malenia", "Orphan of Kos", "Artorias"]
    bosses.insert(len(bosses), "Radahn")
    bosses.insert(0, "Manus")
    print(bosses)

    try:
        bosses.remove("Elden Beast")
    except ValueError as e:
        print(e)

    try:
        # print(f"My favourite boss in Elden Ring is {bosses.pop(len(bosses) - 1)}")
        print(f"My favourite boss in Elden Ring is {bosses.pop(6)}")

    except IndexError as e:
        print(e)

    bosses.clear()
    print(bosses)

    try:
        print(f"Radahn is at index: {bosses.index('Radahn')}")
    except ValueError as e:
        print(e)

    print([1, 2, 3, 3, 4].count(3))
    print(list(range(0, 10)).reverse())


if __name__ == "__main__":
    main()
