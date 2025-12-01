class iterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __next__(self):
        res = self.i
        if res >= self.n:
            raise StopIteration
        self.i = res + 1
        return res

    def __iter__(self):
        return self


def main():
    c_iter = iterator(list(range(0, 10)))

    for _ in c_iter:
        print(_)


if __name__ == "__main__":
    main()
