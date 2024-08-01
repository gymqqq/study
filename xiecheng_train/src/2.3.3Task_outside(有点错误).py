import asyncio
async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


task_list = [
    asyncio.ensure_future(func()),
    asyncio.ensure_future(func())
]  # 放里面放外面效果一样
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task_list))
# done = asyncio.run(asyncio.wait(task_list))
# print(done)

