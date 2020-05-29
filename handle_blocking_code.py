import time, asyncio, concurrent.futures

loop = asyncio.get_event_loop()
blocking_tasks_qty = 30
process_qty = blocking_tasks_qty

"""
    asyncio.run_in_executor example. 
    It runs concurrently blocking and async functions at once
    In case of blocking_tasks_qty > process_qty, only process_qty number of tasks
    will start, others will wait till there are some free processes in 
    the pool.
"""

def some_blocking_func(n):
    print(f'sync function {n} has started')
    time.sleep(10)
    print(f'sync function {n} has finished')


async def some_async_func():
    while True:
        print('hello from async func')
        await asyncio.sleep(0.5)


async def main():
    tasks = []
    with concurrent.futures.ProcessPoolExecutor(process_qty) as pool:
        for n in range(blocking_tasks_qty):
            tasks.append(loop.run_in_executor(pool, some_blocking_func, n))
        tasks.append(some_async_func())

        await asyncio.gather(*tasks)



if __name__ == '__main__':
    loop.run_until_complete(main())