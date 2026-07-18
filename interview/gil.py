import threading
import multiprocessing
import time

# The GIL (Global Interpreter Lock) is a single mutex per CPython process that
# only lets one thread execute Python bytecode at a time -- even on a
# multi-core machine. It exists because CPython's reference counting (see
# memory_management.py) isn't thread-safe: two threads incrementing/
# decrementing the same object's refcount at once would race and corrupt it.
# One global lock around bytecode execution was a simple fix that made the
# rest of the interpreter (and every C extension) much easier to write.


def cpu_bound(n):
    # Busy work with no I/O -- pure bytecode execution, so this holds the GIL
    # for its entire duration.
    count = 0
    for _ in range(n):
        count += 1
    return count


def io_bound(seconds):
    # time.sleep() releases the GIL while blocked, which is exactly why
    # threading helps here but not for cpu_bound().
    time.sleep(seconds)


N = 20_000_000
SLEEP = 0.5
WORKERS = 4


# Everything below is guarded by __name__ == "__main__" because
# multiprocessing (below) uses the "spawn" start method on macOS/Windows --
# each child process re-imports this module from scratch. Without the guard,
# every child would re-run the threading/timing demos too, not just the
# process-pool code.
if __name__ == "__main__":
    # --- CPU-bound: single thread vs multiple threads -----------------------
    # Expectation: threading gives no speedup (often slightly worse, due to
    # lock handoff overhead) because only one thread ever runs Python
    # bytecode at once, regardless of how many threads or cores exist.

    start = time.perf_counter()
    cpu_bound(N * WORKERS)
    single_thread_time = time.perf_counter() - start
    print(f"CPU-bound, single thread ({WORKERS}x work): {single_thread_time:.3f}s")

    start = time.perf_counter()
    threads = [threading.Thread(target=cpu_bound, args=(N,)) for _ in range(WORKERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    multi_thread_time = time.perf_counter() - start
    print(f"CPU-bound, {WORKERS} threads:            {multi_thread_time:.3f}s  (no real speedup -- GIL serializes them)")

    print("---")

    # --- I/O-bound: sequential vs multiple threads ---------------------------
    # Expectation: threading DOES help here. Each thread releases the GIL
    # while blocked in time.sleep(), so the sleeps overlap instead of
    # stacking up.

    start = time.perf_counter()
    for _ in range(WORKERS):
        io_bound(SLEEP)
    sequential_io_time = time.perf_counter() - start
    print(f"I/O-bound, sequential ({WORKERS}x sleeps): {sequential_io_time:.3f}s")

    start = time.perf_counter()
    threads = [threading.Thread(target=io_bound, args=(SLEEP,)) for _ in range(WORKERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    threaded_io_time = time.perf_counter() - start
    print(f"I/O-bound, {WORKERS} threads:              {threaded_io_time:.3f}s  (sleeps overlap -- GIL released during I/O)")

    print("---")

    # --- CPU-bound: multiprocessing bypasses the GIL entirely ---------------
    # Each process gets its own interpreter and its own GIL, so they run
    # truly in parallel on separate cores. This is the standard fix for
    # CPU-bound work.
    start = time.perf_counter()
    processes = [multiprocessing.Process(target=cpu_bound, args=(N,)) for _ in range(WORKERS)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    multiprocess_time = time.perf_counter() - start
    print(f"CPU-bound, {WORKERS} processes:          {multiprocess_time:.3f}s  (real parallelism -- separate GILs)")

    print("---")
    print("Rule of thumb: I/O-bound -> threading (or asyncio), since the GIL is")
    print("released during blocking calls anyway. CPU-bound -> multiprocessing")
    print("(or a C extension/numpy op that releases the GIL), since that's the")
    print("only way to actually use multiple cores for pure Python bytecode.")
