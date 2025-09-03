import asyncio
from datetime import datetime
import click


async def sleep_and_print(seconds):
    print(f"starting async {seconds} 😴")
    await asyncio.sleep(seconds)
    print(f"finished async {seconds} ⌚")
    return seconds


async def main():
    coroutines_list = [sleep_and_print(i) for i in range(1, 11)]
    results = await asyncio.gather(*coroutines_list)
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, fg="black", bg="green")
