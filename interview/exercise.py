def chunked(iterable, size):
    bucket = []
    for item in iterable:
        bucket.append(item)
        if len(bucket) == size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket

def filter_gen(iterable, predicate):
    for item in iterable:
        if predicate(item):
            yield item

def take(iterable, n):
    iterator= iter(iterable)
    for _ in range(n):
        try:
            yield next(iterator)
        except StopIteration:
            return

def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

def pairwise(iterable):
    iterator = iter(iterable)
    try:
        prev = next(iterator)
    except StopIteration:
        return
    for item in iterator:
        yield (prev, item)
        prev = item

def process_log_lines(lines, batch_size):
    """
    lines: an iterable of raw string lines (some malformed, e.g. empty strings)
    Should: filter out empty/whitespace-only lines, then yield them in batches
    of batch_size
    """
    bucket = []
    for item in lines:
        if item.strip():
            bucket.append(item)
            if len(bucket) == batch_size:
                yield bucket
                bucket = []
    if bucket:
        yield bucket

print(list(chunked([1, 2, 3, 4, 5, 6, 7], 3)))
print(list(filter_gen([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)))
print(list(take(infinite_counter(), 5)))
print(list(pairwise([1, 2, 3, 4])))
raw_lines = ["log1", "", "log2", "log3", "  ", "log4", "log5"]
print(list(process_log_lines(raw_lines, 2)))

