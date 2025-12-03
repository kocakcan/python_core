def number_generator(n):
    for i in range(n):
        yield i


def range_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1


def main():
    gen = number_generator(3)
    print(next(gen))
    print(next(gen))
    print(next(gen))

    try:
        print(next(gen))
    except StopIteration:
        print("That's all folks!")

    range_gen = range_generator(0, 10)
    print(next(range_gen))
    print(next(range_gen))

    # Generator Expression
    squares = (x * x for x in range(5))
    print(next(squares))

    names = ["Seyfi", "Leyli", "Dilan", "Medet", "Can"]
    ages = (59, 55, 33, 33, 28)
    dict_comprehension = {key: val for key, val in zip(names, ages)}
    print(f"I'm {dict_comprehension['Can']} years old.")

    try:
        print(dict_comprehension["Malenia"])
    except KeyError:
        print("No such key exists you fuck")

    print(dict_comprehension.get("Malenia", "It doesn't exist"))

    name = "Can Kocak Kocak"
    print(name.count("Kocak", 5))
    print("".join(name))


if __name__ == "__main__":
    main()
