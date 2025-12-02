class iterator:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        value = self.data[self.i]
        self.i += 1
        return value

    def __iter__(self):
        return self


def main():
    c_iter = iterator(list(range(0, 10)))

    for _ in c_iter:
        print(_)


if __name__ == "__main__":
    main()
