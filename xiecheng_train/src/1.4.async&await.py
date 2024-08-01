import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)  # 遇到T0耗时操作，自动化切换到tasks中的其他任务
    # await 等待
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)  # 遇到T0耗时操作，自动化切换到tasks中的其他任务
    print(4)

tasks = {  # 将2个协程函数打包成一个tasks列表 通过run_until_complete执行
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
}

# loop = asyncio.get_event_loop()
# loop.run_until_complete(func1())#只有这两行才能执行协程函数

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# 执行结果 1 3 2 4