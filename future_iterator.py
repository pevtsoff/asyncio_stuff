import asyncio

"""
    Simple Future-like object that can be awaited in a coroutine
    and used as an iterator as well.
"""

class MyAwaitable:
    def __init__(self, start=2):
        self.num = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        if num <= 5:
            self.num += 1
        else:
            raise StopIteration()
        return num

    def __await__(self, *args, **kwargs):
        print(f'{args=}, {kwargs=}')
        print(f"{self.__class__} is awaited!")

        return self.myAsyncMeth().__await__()


    async def myAsyncMeth(self):
        await asyncio.sleep(1)
        return 'result from myAsyncMeth'


async def myCoro():
    cl = await MyAwaitable()
    print(f'MyAwaitable result: {cl}')
    for i in MyAwaitable():
        print(i)


asyncio.run(myCoro(), debug=True)

