def chunked(iterable, size):
    bucket = []
    for item in iterable:
        bucket.append(item)
        if len(bucket) == size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket

print(list(chunked([1, 2, 3, 4, 5, 6, 7], 3)))

