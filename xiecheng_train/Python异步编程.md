# 1.协程

协程不是计算机提供，程序员人为创造。

协程，也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行(用一个线程在代码之间游走的运行)。例如:

```python
def func1():
    print(1)
    ...
    print(2)
def func2():
    print(3)
    ...
    print(4)
func1()
func2()
```

实现协程的方法：

- greenlet：早期模块。
- yield关键字。
- asyncio装饰器(py3.4)
- async、await关键字(py3.5)【推荐】

## 1.1 greenlet实现协程

```python
pip3 install greenlet
```

```python
from greenlet import greenlet

def func1():
	print(1)					#第2步:输出 1
	gr2.switch()				#第3步:切换到 func2 函数
	print(2)					#第6步:输出 2
	gr2.switch()				#第7步:切换到 func2 函数，从上一次执行的位置继续向后执行

def func2():
	print(3)					#第4步:输出 3
	gr1.switch()				# 第5步:切换到 func1 函数，从上一次执行的位置继续向后执行
	print(4)					#第8步:输出 4
	
gr1= greenlet(func1)
gr2= greenlet(func2)
gr1.switch()#第1步:去执行func1 函数
# 输出结果 1 3 2 4
```

## 1.2 yield关键字

```python
def func1():
	yield 1 #生成器函数，只要执行则返回一个生成器
	yield from func2()#跳到func2函数
	yield 2
    
def func2():
	yield 3
	yield 4
    
f1 = func1()
for item in f1:#对生成器进行循环
	print(item)
#输出结果 1 3 4 2
```

## 1.3 asyncio
在python3.4以及之后的版本。

```python
import asyncio

@asyncio.coroutine #通过装饰器给函数装饰一下 coroutine:协程
				 #本来是一个普通函数，加上coroutine之后变成协程函数
def func1():
	print(1)
	yield from asyncio.sleep(2) # 遇到T0耗时操作，自动化切换到tasks中的其他任务
    #asyncio.sleep(2) 等2秒，但是等的时候可以切换到func2，切换到其他任务
    #2秒之后继续执行
    print(2)
    
@asyncio.coroutine
def func2():
    print(3)
	yield from asyncio.sleep(2)# 遇到T0耗时操作，自动化切换到tasks中的其他任务
    print(4)
tasks ={#将2个协程函数打包成一个tasks列表 通过run_until_complete执行
	asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
}

#loop = asyncio.get_event_loop()
#loop.run_until_complete(func1())#只有这两行才能执行协程函数

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
#执行结果 1 3 2 4
```

注意：遇到IO阻塞自动切换，前面2种都是手动切换

​            省时间，如果不使用asyncio，需要4秒；使用之后，只需要2秒。

## 1.4 async & await  关键字

在python3.5及之后的版本。(与1.3本质相同，但是引入两个关键字，更加方便)

```python
import asyncio

async def func1():
	print(1)
	await asyncio.sleep(2) # 遇到T0耗时操作，自动化切换到tasks中的其他任务
    #await 等待
    print(2)
    
async def func2():
    print(3)
	await asyncio.sleep(2)# 遇到T0耗时操作，自动化切换到tasks中的其他任务
    print(4)
tasks ={#将2个协程函数打包成一个tasks列表 通过run_until_complete执行
	asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
}

#loop = asyncio.get_event_loop()
#loop.run_until_complete(func1())#只有这两行才能执行协程函数

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
#执行结果 1 3 2 4
```

# 2.协程意义

在一个线程中，如果遇到IO等待时间，线程不会傻傻等，利用空闲时间再去干点其他的事。

案例：去下载三张图片(网络IO)

- 普通方式(同步)

```python
import requests
def download_image(url):
    print("开始下载:"，url)
    # 发送网络请求，下载图片
	response = requests.get(url)
    print("下载完成")
    # 图片保存到本地文件
	file name = url.rsplit('_')[-1]
    with open(file name, mode='wb')as file_object:
        file_object.write(response.content)
if __name__ == '__main__':
    url list =[
        'https://wmw3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90 0 autohomecar,ChsEe12AXQ6A0OH AAFOCMs8nzU621.jpg',
        'https: //www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90 0 autohomecar ChcCSV2BBICAUntfAADjJFd6808429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M08/3c/65/120x90 0 autohomecarChCCP12BFCmAIO83AAGG7VKOSGY193.jpg
    ]
for item in url_list:
    download_image(item)
```

- 协程方式(异步)

~~~python
import aiohttp
import asyncio
async def fetch(session, url):
    print("发送请求:"，url)
    async with session.get(url,verify_ssl=False)as response:
        content = await response.content.read()
        file_name =url.rsplit('_')[-1]
        with open(file_name, mode='wb')as file_object:
            file_object.write(content)
            print('下载完成',url)
async def main():
	async with aiohttp.ClientSession()as session:
		url_list =[
			'https://wmw3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0 autohomecarChSEe12AXQ6AOOH AAFOCMS8nzU621.jpg',
            'https: //wmw2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0 autohomecar chcCSV2BBICAUntfAADjJFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M08/3c/65/120x90 0 autohomecar ChCCP12BFCMAI083AAGG7VKOSGY193.jpg'
        ]
		tasks =[ asyncio.create_task(fetch(session, url))for url in url_list ]
		await asyncio.wait(tasks)
if __name__ == '__main__ ':
    asyncio.run( main())
~~~



# 3.**asyncio模块进行异步编程**



## 3.1 事件循环

理解成为一个死循环，去检测并执行某些代码。

```
# 伪代码

任务列表=[任务 任务2，任务3,...]

while True:
	可执行的任务列表，已完成的任务列表 =去任务列表中检查所有的任务，将'可执行'和'已完成"的任务返回
	
	for 就绪任务 in 已准备就绪的任务列表:
		执行已就绪的任务
	for 已完成的任务 in 已完成的任务列表:
	在任务列表中移除 已完成的任务
	
如果任务列表中的任务都已完成，则终止循环
```

~~~python
import asyncio

#去生成或获取一个事件循环
loop = asyncio.get_event_loop()

#将任务放到“任务列表”
loop.run_until_complete(任务)
~~~

## 3.2 快速上手

协程函数，定义函数： async def 函数名。

协程对象，执行 协程函数() 得到的协程对象。

~~~python
async def func():
    pass

result = func()
~~~

注意：执行协程函数创建协程对象，函数内部代码不会执行。

如果想要运行协程函数内部代码，必须要将协程对象交给事件循环来处理。

~~~python
import asyncio
async def func():
    print()
result = func()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(result)
asyncio.run(result) #等于上面两行 python3.7之后
~~~

## 3.3 await

await + 可等待的对象(协程对象、Future、Task对象 --> IO等待)

示例1：

~~~python
import asyncio
async def func():
    print()
    response = await asyncio.sleep(2)
    print("结果",response)
    
asyncio.run(func())
~~~

示例2：

~~~python
import asyncio
async def others():
	print("start")
	await asyncio.sleep(2)
	print('end')
	return '返回值'
async def func():
	print("执行协程函数内部代码")
# 遇到IO操作挂起当前协程(任务)，等I0操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程(任务)。
	response = await others()
	print("IO请求结束，结果为:"，response)
asyncio.run( func())
~~~

示例3：

~~~python
import asyncio
async def others():
	print("start")
	await asyncio.sleep(2)
	print('end')
	return '返回值'
async def func():
	print("执行协程函数内部代码")
# 遇到IO操作挂起当前协程(任务)，等I0操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程(任务)。
	response1 = await others() 
	print("IO请求结束，结果为:"，response1)
    response2 = await others()
	print("IO请求结束，结果为:"，response2)
asyncio.run( func())
~~~

await 就是等待对象的值得到结果之后再继续向下走。

## 3.4 Task对象

*Tasks are used to schedule coroutines concurrently.*
*When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine isautomatically scheduled to run soon.*

在事件循环中添加多个任务的，

Tasks用于**并发**调度协程，通过**asyncio.create_task**(协程对象)的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。除了使用 **asyncio.create_task()**函数以外，还可以用低层级的loop.create_task()或 ensure_future()函数。不建议手动实例化 Task 对象。

注意:asyncio.create_task()函数在 Python 3.7中被加入。在 Python 3.7 之前，可以改用低层级的asyncio.ensure_future()函数。

示例1：

~~~python
import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

async def main():
    print("main开始")

    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task1 = asyncio.create_task(func())
    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task2 = asyncio.create_task(func())
    print("main结束")

    # 当执行某协程遇到I0操作时，会自动化切换执行其他任务。
    # 此处的await是等待相对应的协程全都执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)
asyncio.run(main())
~~~

示例2：

~~~python
import asyncio
async def func():
	print(1)
	await asyncio.sleep(2)
	print(2)
	return '返回值'
async def main():
	print("main开始")
    task_list = [
        asyncio.create_task(func(),name = 'n1')
        asyncio.create_task(func(),name = 'n2')
    ]
    
	print("main结束")
	done.pending = await asyncio.wait(task_list,timeout = None)#最多等几秒
    print(done)
async.run(main())
~~~

示例3:

~~~python
import asyncio
async def func():
	print(1)
	await asyncio.sleep(2)
	print(2)
	return “返回值”

task_list = [
    func(),
    func(),
]#放里面放外面效果一样
done,pending = asyncio.run(asyncio.wait(task_list))
print(done)
~~~

## 3.5 asyncio.Future对象

> A Future is a special low-level awaitable object that represents an eventual result of an
> asynchronous operation.

Task继承Future，Task对象内部await结果的处理基于Future对象来的。

示例1:

~~~python
async def main():
	# 获取当前事件循环
	1oop = asyncio.get_running_1oop()
	# 创建一个任务(Future对象)，这个任务什么都不干。
    fut =loop.create_future()
	# 等待任务最终结果(Future对象)，没有结果则会一直等下去。
    await fut
asyncio.run(main())
~~~

示例2:

~~~python
import asyncio
async def set_after(fut):
	await asyncio.sleep(2)
	fut.set_result("666")
async def main():
	# 获取当前事件循环
	loop=asyncio.get_running_loop()
	#创建一个任务(Future对象)，没绑定任何行为，则这个任务永远不知道什么时候结束。
	fut =loop.create_future()
	# 创建一个任务(Task对象)，绑定了set_after函数，函数内部在2s之后，会给fut赋值。
	#即手动设置future任务的最终结果，那么fut就可以结束了。
	await loop.create_task(set_after(fut))
	# 等待 Future对象获取 最终结果，否则一直等下去
	data = await fut
	print(data)
asyncio.run( main())
~~~

## 3.6 concurrent.futures.Future对象

(与3..5无关)

使用线程池、进程池实现异步操作时用到的对象。

~~~python
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent,futures.process import ProcessPoolExecutor
def func(value):
	time.sleep(1)
	print(value)
#创建线程池
pool = ThreadPoolExecutor(max_workers=5)
#或创建进程池
#pool = ProcessPoolExecutor(max_workers=5)
for i in range(10):
    fut = pool.submit(func,i)
    print(fut)
~~~

以后写代码可能会存在交叉使用。例如：arm项目80%都是基于协程异步编程 + Mysql(不支持)【线程、进程做异步编程】。

~~~python
import time
import asyncio
import concurrent.futures

def func1():
# 某个耗时操作
	time.s1eep(2)
	return "6"
async def main():
	1oop=asyncio.get_running_1oop()
# 1. Run in the default loop's executor( 默认ThreadPoolExecutor )
#第一步:内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
#第二步:调用asyncio,wrap_future将concurrent.futures.Future对象包装为asycio.Future对象。
#因为concurrent.futures.Future对象不支持await语法，所以需要包装为 asycio.Future对象 才能使用。
	fut = loop.run_in_executor(None,func1)
	result = await fut
	print('default thread pool',resu1t)
	#2.Run in a custom thread pool:
	#with concurrent.futures.ThreadPoolExecutor() as pool:
	#	result=await loop.run_in_executor(
	#		pool，func1)
    #	print('custom thread pool',result)

	# 3. Run in a custom process pool:
	#with concurrent.futures,ProcessPoolExecutor() as pool:
    #	result=await loop.run_in_executor(pool，func1)
    #	print('custom process pool',result)
asyncio.run( main())
~~~

示例：asyncio + 不支持异步的模块

~~~python
import asyncio
import requests
async def download_image(url):
#发送网络请求，下载图片(遇到网络下载图片的IO请求，自动化切换到其他任务)
	print("开始下载:"，ur1)
	loop=asyncio.get_event_1oop()
# requests模块默认不支持异步操作，所以就使用线程池来配合实现了future =loop.run_in_executor(None,requests.get, ur1)
	response =await future
	print('下载完成')
	# 图片保存到本地文件
	file_name = url.rsplit('_')[-1]
	with open(file_name,mode='wb')as file_object:
		file_object.write(response.content)
        
if __name__=='__main__':
    url_list =[
'https://ww3,autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar_ChSEe12AXQ6AOOH_AAFOCMS8nzu621.jpg',
'https: //www2.autoimg.cn/newsdfs/g30/M01/3c/E2/120x90_0_autohomecar_chccsV2BBICAUntfAADjJFd6800429.jpg'，
'https: //www3,autoimg.cn/newsdfs/g26/M0B/3c/65/120x90_0_autohomecar_ChCCP12BFCMAIO83AAGq7VK0sGY193.jpg'
    ]
	tasks=[download_image(url) for url in url_list]
	1oop =asyncio.get_event_1oop()
    loop.run_until_complete( asyncio.wait(tasks))
~~~

## 3.7 异步迭代器

什么是异步迭代器

实现了aiter_()和_anext_()方法的对象。_anext_必须返回一个 awaitable 对象。async for 会处理异步迭代器的 anext_()方法所返回的可等待对象，直到其引发一个 stopAsyncIteration 异常。由PEP 492 引入。

什么是异步可迭代对象?
可在 async for 语句中被使用的对象。必须通过它的aiter_()方法返回一个 asynchronous iterator。由PEP 492 引入。

~~~python
import asyncio
class Reader(object):
    #自定义异步迭代器(同时也是异步可迭代对象)
	def _init_(self):
        self.count =0
	async def readline(self):
    	# await asyncio.sleep(1)
        self.count +=1
        if self.count == 100:
            return None
		return self.count
    
	def __aiter__(self):
    	return self
    
	async def __anext__(self):
        val= await self.readline()
        if val == None:
            raise stopAsyncIteration
        return val
    
async def func():
	obj = Reader()
	async for item in obj:
    	print(item)
        
asyncio.run(func())
~~~

## 3.8 异步上下文管理器

此种对象通过定义aenter_()和-aexit_()方法来对 async with 语句中的环境进行控制。由 PEP 492引入。

~~~python
import asyncio
class AsynccontextManager:
    def __init__(self):
        self.conn =conn
	async def do_something(self):
        #异步操作数据库
        return 666
	async def __aenter__(self):
        #异步链接数据库
		self.conn = await asyncio.sleep(1)
		return self
		async def __aexit__(self,exc_type,exc, tb):
            # 异步关闭数据库链接
		await asyncio.sleep(1)
        
async def func():
    async with AsyncContextManager() as f:
    	result = await f.do_something()
    	print(result)
        
asyncio.run(func())
~~~

# 4.uvloop

是asyncio的事件循环的替代方案。事件循环 > 默认asyncio的事件循环。

~~~python
pip3 install uvloop
~~~

~~~python
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#编写asyncio的代码，和之前写的代码一致

#内部的时间循环自动化会变成uvloop
asyncio.run(...)
~~~

注意:一个asgi->uvicorn 内部使用的就是uvloop
