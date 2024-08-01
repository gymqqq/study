def func1():
    yield 1  # 生成器函数，只要执行则返回一个生成器
    yield from func2()  # 跳到func2函数
    #从func2()函数中来进行生成
    yield 2
#yield函数可以理解为不输出的输出函数。相当于存储一个值，但是不输出

def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:  # 对生成器进行循环
    print(item)
# 输出结果 1 3 4 2