import asyncio
async def main():
	# 获取当前事件循环
	loop = asyncio.get_running_loop()
	fut = loop.create_future()
	# 创建一个任务(Future对象)，这个任务什么都不干。
	# fut = asyncio.get_running_loop().create_future()
	# 等待任务最终结果(Future对象)，没有结果则会一直等下去。
	await fut
asyncio.run(main())