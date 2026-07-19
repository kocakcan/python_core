import asyncio
import time

# async/await is Python's syntax for COOPERATIVE concurrency on a SINGLE
# thread. An event loop (started by asyncio.run) juggles many coroutines:
# whenever one of them hits `await` on something that isn't ready yet
# (a network response, a timer), it SUSPENDS and hands control back to the
# loop, which runs whichever other coroutine is ready. Nothing is ever
# interrupted mid-statement -- switches only happen at `await` points.
# Contrast with threading (see gil.py), where the OS preempts threads
# whenever it likes and the GIL serializes the bytecode anyway.


# --- 1. A coroutine is an object, not a running thing ----------------------
# `async def` does NOT run the body when called. Calling it just builds a
# coroutine object -- exactly like how calling a generator function builds a
# generator without running it (see generators_and_iterators.py). In fact
# coroutines evolved from generators: both are resumable frames that can
# suspend (`yield` / `await`) and be resumed later.

async def fetch(name, seconds):
    # Stand-in for an I/O call (HTTP request, DB query). asyncio.sleep is
    # the async version of time.sleep: it tells the loop "wake me in N
    # seconds" and suspends, letting other coroutines run meanwhile.
    print(f"  {name}: started")
    await asyncio.sleep(seconds)
    print(f"  {name}: finished after {seconds}s")
    return name


coro = fetch("demo", 1)
print(f"Calling an async def gives: {coro}")
print("...and the body hasn't run at all (no 'started' printed above).")
# Gotcha #1: forgetting `await`. The coroutine object is created, never
# scheduled, and silently does nothing except emit a RuntimeWarning:
# "coroutine 'fetch' was never awaited". Close it here to avoid that warning:
coro.close()
print("---")


# --- 2. Sequential awaits vs asyncio.gather --------------------------------
# Awaiting coroutines one-by-one is still fully sequential -- each await
# waits for completion before starting the next, just like normal calls.
# Concurrency only happens when multiple coroutines are IN FLIGHT at once,
# which is what asyncio.gather (or asyncio.TaskGroup) arranges: it schedules
# them all, then waits; while one sleeps, the loop runs the others.
# Same shape as the sequential-vs-threaded sleep timing in gil.py.

async def sequential():
    for i in range(3):
        await fetch(f"seq-{i}", 0.5)


async def concurrent():
    results = await asyncio.gather(*(fetch(f"con-{i}", 0.5) for i in range(3)))
    print(f"  gather returned results in order: {results}")


start = time.perf_counter()
asyncio.run(sequential())  # asyncio.run = create loop, run coroutine, close loop
print(f"Sequential awaits, 3 x 0.5s sleeps: {time.perf_counter() - start:.2f}s (they stack up)")
print("---")

start = time.perf_counter()
asyncio.run(concurrent())
print(f"asyncio.gather, 3 x 0.5s sleeps:    {time.perf_counter() - start:.2f}s (they overlap)")
print("---")


# --- 3. Gotcha #2: blocking calls freeze the WHOLE loop --------------------
# The loop can only switch coroutines at await points. A plain blocking call
# (time.sleep, requests.get, heavy computation) never yields control, so
# every other coroutine is stuck until it returns -- concurrency is gone.
# This is THE classic async bug: one sync library call in an async service
# stalls every request. Fixes: use an async library (aiohttp instead of
# requests), or push the blocking call to a thread with asyncio.to_thread().

async def blocking_fetch(name, seconds):
    print(f"  {name}: started")
    time.sleep(seconds)  # BLOCKS the event loop -- nothing else can run
    print(f"  {name}: finished after {seconds}s")


async def blocked_concurrent():
    await asyncio.gather(*(blocking_fetch(f"blk-{i}", 0.5) for i in range(3)))


start = time.perf_counter()
asyncio.run(blocked_concurrent())
print(f"gather but with time.sleep:         {time.perf_counter() - start:.2f}s (blocking call -> sequential again)")
print("---")


# --- 4. asyncio vs threading vs multiprocessing ----------------------------
# All three attack "do many things at once", but differently:
#
#              asyncio                threading              multiprocessing
#   unit       coroutine              OS thread              OS process
#   switching  cooperative (await)    preemptive (OS)        true parallel
#   GIL        irrelevant: 1 thread   GIL serializes         one GIL per process
#   memory     lightest (a frame)     ~MB stack per thread   heaviest
#   best for   MANY slow I/O waits    I/O with sync-only     CPU-bound work
#              (10k connections)      libraries              (see gil.py)
#
# Extending gil.py's rule of thumb: I/O-bound with async-capable libraries
# and/or huge connection counts -> asyncio; I/O-bound but stuck with
# blocking libraries -> threading; CPU-bound -> multiprocessing. asyncio
# does NOT help CPU-bound code at all -- it's still one thread under the GIL.


# --- 5. The 30-second verbal answer ----------------------------------------
# "async/await is cooperative concurrency on a single thread. `async def`
# creates a coroutine -- a resumable function built on the same machinery as
# generators. An event loop runs coroutines, and `await` marks the points
# where one can suspend while waiting on I/O so the loop can run others;
# asyncio.gather is how you actually get several in flight at once. It's
# concurrency, not parallelism: one thread, so the GIL never matters, but a
# single blocking call freezes everything, and CPU-bound work gains nothing
# -- that's what multiprocessing is for."
