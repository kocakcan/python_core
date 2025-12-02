def fib_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    for _ in fib_generator(10):
        print(_)


if __name__ == "__main__":
    main()
