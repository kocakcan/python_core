from functools import cache


@cache
def fib(n: int) -> int:
    if n < 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    print(fib(100))


if __name__ == "__main__":
    main()
