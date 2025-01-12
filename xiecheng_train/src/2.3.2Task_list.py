import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

async def main():
    print("main开始")

    task_list = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]
    print("main结束")
    done = await asyncio.wait(task_list, timeout=None)  # 最多等几秒
    print(done)
asyncio.run(main())