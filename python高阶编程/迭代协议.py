# 协议 ： 与其他编程语言中的接口很相似,规定哪些地方必须要定义
# 协同程序 : 可以暂停，挂起，然后从上次暂停的地方开始执行

# 迭代器
'''
迭代协议 : 可迭代类型与迭代器
迭代器（Iterable） 只是对象每次返回特定成员的一种能力。
迭代器 : 访问集合内元素的一种方式，一般用来遍历数据
迭代器 和 下标 的访问方式不一样，迭代器是不能返回的 (list[1][0]) 提供了一种惰性访问数据的方式
可迭代类型中包含了__iter__但不是迭代器，迭代器必须要有__next__

'''
from collections.abc import Iterable,Iterator
list1 = [1,2]
isinstance(list1,Iterator) # False
isinstance(list1,Iterable) # True

# 生成器
# 生成器高阶看协程介绍.py
'''
生成器 : 迭代器的一种，但不用 class 只需要一个 yield 即可
列表推导式，字典推导式，生成器推导式 <- 就是元组推导式 (i for i in range(10))
一旦函数将控制权交还给调用者，就意味着全部结束。函数中做的所有工作以及保存在局部变量中的数据都将丢失。再次调用这个函数时，一切都将从头创建。
return 隐含的意思是函数正将执行代码的控制权返回给函数被调用的地方。而 yield 的隐含意思是控制权的转移是临时和自愿的，我们的函数将来还会收回控制权。
生成器就是一类特殊的迭代器。
'''

# 符号分隔开来的一行文本文档的读取 (适合读取超大文件)
def myreadlines(f,newline):
    # 第二遍循环开始，buf.index定位到 '{|}' 然后 yield 出来
    buf = "" # 缓存
    while True:
        while newline in buf: # 检测缓存中是否存在分隔符
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):] # 如果一开始4096*10读取到了几个分隔符，需要将他们分几行
        chunk = f.read(4096*10) # 首先进入到这里(buf="") 一开始读取4096*10
        if not chunk:
            # if not 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk

# with open("input.txt") as f:
#     for line in myreadlines(f,"{|}"):
#         print(line)

# 传统函数调用 A->B (A用完到B)
# 需要一个可以暂停的函数,并且可以在适当的时候恢复并继续执行
# 出现了协程 -> 有多个入口的函数,可以暂停的函数,可以向暂停的地方传入值
'''
生成器高阶
throw : 在生成器暂停的地方抛出类型为 type 的异常，并返回下一个 yield 的返回值。
        1.一开始用send()启动生成器必须要send(None)
close : 在生成器函数暂停的地方抛出一个 GeneratorExit 异常。
send : 向生成器发送一个值，随后恢复执行。
'''

# 67
# !/usr/bin/python3
# ----------send
# def MyGenerator():
#         value=yield 1
#         yield value
#         return 1
#
# gen=MyGenerator()
# print(next(gen))
# print(gen.send("I am Value"))
'''
next(gen)和send() 都可以启动生成器
1. next(gen)启动生成器并且到达了yield 1 这个位置返回1并停住
2. gen.send("") 传入字符串并且运行 value= 然后返回 value这个值并停住
'''

# -----------throw

# def gen_func():
#     # 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
#     try:
#         yield 0
#     except Exception as e:
#         print("1")
#     for i in range(2,10):
#         yield i
#
#     return "bobby"
#
# if __name__ == "__main__":
#     # throw完后在当前停在的那个yield语句那里报错
#     # throw后找不到except会报错,找到后执行完里面的语句总会跳过一个yield 并且返回跳过后的下一个yield返回值
#     gen = gen_func()
#     print(next(gen))
#     gen.throw(Exception, "download error") # yield 2会跳过
#     print(next(gen))
#     #gen.throw(Exception, "download error")


# def gen():
#     n = 0
#     while True:
#         try:
#             yield n
#             n += 1
#         except ZeroDivisionError:
#             print('捕获到了 ZeroDivisionError')
#             print('此时的 n 为：%s' % n)
#
# g = gen()
# ret = next(g)
# print('第一次 yield 的返回值：%s' % ret)
# """
# 第一次 yield 的返回值：0
# """
#
# print()
# ret = g.throw(ZeroDivisionError)
# print('第二次 yield 的返回值：%s' % ret)
# """
# 捕获到了 ZeroDivisionError
# 此时的 n 为：0
# 第二次 yield 的返回值：0
# """
#
# print()
# ret = next(g)
# print('第三次 yield 的返回值：%s' % ret)
# """
# 第三次 yield 的返回值：1
# """

# *-----------close
# 当except语句块处理完毕后，系统会继续往下执行，直至生成器方法执行结束。
# 需要注意的是，GeneratorExit异常的产生意味着生成器对象的生命周期已经结束。
# 因此，一旦产生了GeneratorExit异常，生成器方法后续执行的语句中，不能再有yield语句，否则会产生RuntimeError。
# def myGenerator():
#     try:
#         yield 1
#         print("Statement after yield")
#     except GeneratorExit:
#         print("Generator error caught")
#     print("End of myGenerator")
# gen = myGenerator()
# print(next(gen))
# gen.close()
# print("End of main caller"  )

# ------------ yield from语句
'''
yield 返回的只是 那个对象
yield from 返回对象里面的元素

1、调用方：调用委派生成器的客户端（调用方）代码
2、委托生成器：包含yield from表达式的生成器函数
3、子生成器：yield from后面加的生成器函数

yield from 的作用是帮助我们处理异常
子生成器如果是个迭代器则没有send(),throw(),close()方法需要利用双向通道(委托生成器)帮我们完成
'''
from itertools import chain

# chain (能将多个可迭代类型相加起来)
# dict_tttt = {"a": '1',
#              "b": '2'}
#
#
# # for value in chain(dict_tttt,range(5,7)):
# #     print(value)
#
# def my_chain(*args, **kwargs):
#     for iterable in args:
#         yield from iterable
#
#
# for value in my_chain(dict_tttt, range(5, 10)):
#     print(value)
'''
yield from 本质
def my_chain(*args,**kwargs):
    for iterable in args: # (先选出每个可迭代对象)
        for value in iterable: # (在每个可迭代对象中选出里面的元素)
            print(value)
'''

'''
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count

    # 每一次return，都意味着当前协程结束。
    return total,count,average

# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)      # 结束协程
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程

if __name__ == '__main__':
    main()

'''
import inspect
# 生成器实现协程 视频12-11






