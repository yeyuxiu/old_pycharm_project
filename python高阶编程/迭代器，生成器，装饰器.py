# 迭代协议跟元类描述符各种魔法方法 都存在教程

# 迭代器
import time
from collections.abc import Iterable
# Iterable Iter
# isinstance('123',Iterable) # 查看是否可迭代
# list1 = [1, 2, 3, 4]
# it = iter(list1)  # 实例化it 成为迭代器
# print(next(it)) # 利用next 去迭代

# 如果是自定义的类 class __iter__ __next__ 就是迭代器

# 生成器

# () 变成的推导式 产生的对象是 generator 生成器
# 目的是为了 边迭代 边输出值 (大数据输出的时候)
# 有yield 就叫生成器


# 闭包(下面这个叫闭包)
# def logincheck(func):
#     def wrapper():
#         pass
#     return wrapper

# 第一次我们只能 定义两个func 然后里面代码内容大部分相同
# 第二次我们定义了一个函数，然后给func1 func2 传参 但实际上这样还是改变了代码逻辑
# 第三次拥有了装饰器，只需要在func1 func2 上面加个 语法糖



# 装饰器
'''
既不改变函数定义的业务逻辑，又不改变函数调用时的代码
函数定义的改变而不是对函数调用的改变
业务场景是，别人写了一段代码我们不能去动，但我们要增加一些公用的业务逻辑
装饰执行顺序就是装饰器摆放的位置
'''

def logincheck(func):
    def wrapper(*args, **kwargs): # 添加args是为了防止不知道参数有多少个，函数里
        print('login check!')
        func(*args, **kwargs)
    return wrapper

# def timecheck(func):
#     def wrapper():
#         print(time.time())
#         func()
#     return wrapper

# @timecheck
@logincheck
def f1(x):
    print("this is fun1", x)
@logincheck
def f2(**kwargs):
    print("this is fun2")
    print(kwargs)

f1('a')
f2(d=1, b=2, c=3)
