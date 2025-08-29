class People:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age


class Engineer(People):
    def __init__(self, name: str, age: int, occupation: str):
        super().__init__(name, age)
        self._occupation = occupation

    @property
    def occupation(self) -> str:
        return self._occupation

    @occupation.setter
    def occupation(self, occupation: str) -> None:
        self._occupation = occupation


class Developer(Engineer):
    def __init__(
        self, name: str, age: int, occupation: str, programming_languages: list[str]
    ):
        super().__init__(name, age, occupation)
        self._programming_languages = programming_languages

    @property
    def programming_languages(self) -> list[str]:
        return self._programming_languages

    @programming_languages.setter
    def programming_languages(self, programming_languages: list[str]) -> None:
        self._programming_languages = programming_languages


def main():
    me = Developer("Can", 27, "Python Developer", ["C", "C++", "Java", "Python"])
    print(f"My name is {me.name} and I'm a {me.occupation}")
    print(f"The programming languages I know are {', '.join(me.programming_languages)}")
    print(f"My favourite programming language is: {me.programming_languages[0]}")


if __name__ == "__main__":
    main()
