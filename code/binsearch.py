def binsearch(n: list[int], x: int) -> int:
    low = 0
    high = len(n) - 1

    while low <= high:
        mid = (low + high) // 2
        if n[mid] < x:
            low = mid + 1
        elif n[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


def main():
    n = list(range(0, 10))
    print(f"Result: {binsearch(sorted(n), 0)}")
    # Negative
    print(f"Result: {binsearch(sorted(n), 10)}")


if __name__ == "__main__":
    main()
