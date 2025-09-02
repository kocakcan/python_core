# Asynchronous tasks are operations that can be paused while waiting for
# something.
# Common example include:
# - I/O operations (file, network)
# - Database operations
# - API calls
# - Sending emails
# - Long-running calculations

import asyncio
import aiohttp
import smtplib
from email.message import EmailMessage


# Example of async HTTP request
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# Example of async email sending
async def send_email_async(to_email, subject, body):
    # This is just a simulation, simulate network delay
    await asyncio.sleep(1)
    print(f"Email sent to {to_email}")


# Example of async database operation (using asyncpg)
async def fetch_user(user_id):
    await asyncio.sleep(0.1)
    return {"id": user_id, "name": "John Doe"}


# Asynchronous (Single Thread, Concurrent)
async def async_example():
    async def task1():
        await asyncio.sleep(1)
        return "Task 1 done"

    async def task2():
        await asyncio.sleep(1)
        return "Task 2 done"

    # These run concurrently (not parallel)
    results = await asyncio.gather(task1(), task2())
    return results


# Parallel (Multiple Threads/Processes)
from multiprocessing import Pool


def parallel_example():
    def heavy_calculation(x):
        # CPU-bound task
        return sum(i * i for i in range(x))

    # These run in parallel on different CPU cores
    with Pool(2) as p:
        results = p.map(heavy_calculation, [1000000, 2000000])
    return results
