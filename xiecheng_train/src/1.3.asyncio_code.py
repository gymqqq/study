import asyncio


@asyncio.coroutine  # 通过装饰器给函数装饰一下 coroutine:协程
# 本来是一个普通函数，加上coroutine之后变成协程函数
def func1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到T0耗时操作，自动化切换到tasks中的其他任务
    # asyncio.sleep(2) 等2秒，但是等的时候可以切换到func2，切换到其他任务
    # 2秒之后继续执行
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到T0耗时操作，自动化切换到tasks中的其他任务
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