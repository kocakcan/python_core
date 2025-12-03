def main():
    d = {
        "name": "Can",
        "age": 28,
        "is_engineer": True,
        "rate": 0.79,
        "cv_score": 79,
        "hobbies": ["Coding", "Playing video games"],
    }

    d2 = dict([(1, "foo"), (10, "bar")])
    # print(d2)

    name = d["name"]
    print(name)

    try:
        print(d["gender"])
    except KeyError:
        print("No key exists named gender")

    print(d.get("gender", "No key exists named gender"))

    # Update
    d["rate"] = 0.91
    d["hobbies"].append("Playing guitar")

    print(d["hobbies"])
    print(d["rate"])

    # Delete
    try:
        del d["invalid_key"]
    except KeyError:
        print("No such key exists")

    for _ in d.items():
        print(_)

    for _ in d.values():
        print(_)

    # Membership check
    if "hobbies" in d and d["is_engineer"]:
        print("Both keys exist")

    # Dictionary keys should be hashable
    # int, float, string, tuple are all hashable types


if __name__ == "__main__":
    main()
