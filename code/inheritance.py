class MLEngineer:
    def __init__(self, fav_model: str):
        self._fav_model = fav_model


class Parent:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age


class Child(Parent, MLEngineer):
    def __init__(self, name: str, age: int, fav_model: str, occupation: str):
        Parent.__init__(self, name, age)
        MLEngineer.__init__(self, fav_model)
        self._fav_model = fav_model
        self._occupation = occupation


def main():
    child = Child("Can", 28, "Random Forest", "Software Engineer")
    print(f"My name is {child._name}. I'm {child._age} years old.")
    print(f"My favourite model is {child._fav_model}")
    print(f"mro for Child: {Child.__mro__}")


if __name__ == "__main__":
    main()
