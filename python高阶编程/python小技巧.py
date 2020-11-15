# 关于python中一些好用又少用的操作

# # 1. join
# list1 = ['a','b','c','d']
# for i in list1:
#     print(i,end=',') # a,b,c,d
#
# print(','.join(list1)) # a,b,c,d 字符串的拼接
#
# # 2. zip() 场景:合拼两个均等的可迭代对象
# for need in zip([1,2,3],['a','b','c']):
#     print(need)
# '''
# (1, 'a')
# (2, 'b')
# (3, 'c')
# '''


# #3. 普通的序列解包
# a,b,c = 1,2,3
# print(a,b,c)
# # 1 2 3
# #带星号的序列解包(赋值对应位置的两个变量，其余归*)
#
# a,b,*c = 1,2,3,4,5,6,7,8,9
# print(a,b)
# print(c)
# '''
# 1 2
# [3, 4, 5, 6, 7, 8, 9]
# '''
# a,*b,c = 1,2,3,4,5,6,7,8,9
# print(a,c)
# print(b)
# '''
# 1 9
# [2, 3, 4, 5, 6, 7, 8]
# '''
# *a,b,c = 1,2,3,4,5,6,7,8,9
# print(b,c)
# print(a)
# '''
# 8 9
# [1, 2, 3, 4, 5, 6, 7]
# '''

# 4. enumerate
# str1 = 'how many times'
# times = 0
# for i in str1:
#     print(times,i)
#     times += 1
#
# for times,i in enumerate(str1):
#     print(times,i)

# 5.各种推导式
# url =
# 6.collections 模块

'''
此模块实现专用的容器数据类型，提供Python通用内置容器dict的替代品，列表、集合和元组。

* namedtuple   用于创建带有命名字段的元组子类的工厂函数
* deque        列表式容器，两端都有快速的附加和弹出
* ChainMap     用于创建多个映射的单个视图的类dict
* Counter      用于计算哈希对象的dict子类
* OrderedDict  记住订单条目的dict子类被添加
* defaultdict  调用工厂函数以提供缺少的值的dict子类
* UserDict     包装字典对象以便于dict子类化
* UserList     包装列表对象以便于列表子类化
* UserString   包装字符串对象，以便更容易的字符串子类化

源码中直接翻译过来的,还有其他内置函数可以 ctrl+b 点进去看源码
'''
import collections

'namedtuple'
# 可以命名元组
point = collections.namedtuple('point',['x','y'])
p = point(2,1)
# print(p)

'ChainMap'
# 将多个字典合拼
# a = {'x': 1, 'z': 3 }
# b = {'y': 2, 'z': 4 }
# c = collections.ChainMap(a,b)
# print(c['x']) # Outputs 1 (from a)
# print(c['y']) # Outputs 2 (from b)
# print(c['z']) # Outputs 3 (from a)
'deque'
# deque可以高效的实现插入和删除的双向列表，适用于队列和栈。

q= collections.deque(['a','b','c'])
q.append('x')
q.appendleft('y')

'Counter'
# 它是一个无序的容器类型，以字典的键值对形式存储。
# from collections import Counter
# str1 = "bijgtnbjitgnbtgij"
# list1 = [66,88,44,22,22,22,22,'a','a','c']
# dict1 = {'a':1,'b':'2','c':5}
#
# # Counter将元素数量统计，然后计数返回一个字典，键为元素，值为元素个数
#
# print(dict(Counter(str1))) # {'b': 3, 'i': 3, 'j': 3, 'g': 3, 't': 3, 'n': 2}
# print(dict(Counter(dict1))) # {'a': 1, 'b': '2', 'c': 5}
# print(dict(Counter(list1))) # {66: 1, 88: 1, 44: 1, 22: 4, 'a': 2, 'c': 1}
#
# # most_common(int) 返回一个列表，包含counter中n个最大数目的元素，如果忽略n或者为None
#
# print(Counter(str1).most_common(3)) # [('b', 4), ('c', 4), ('a', 3)]
#
# # elements返回一个迭代器，每个元素重复的次数为它的数目，顺序是任意的顺序，如果一个元素的数目少于1，那么elements()就会忽略它
#
# print(type(Counter(str1).elements())) # <class 'itertools.chain'>
# print(''.join(Counter(str1).elements())) # bbbiiijjjgggtttnn
#
# # update 从一个可迭代对象中或者另一个映射（或counter）中所有元素相加
#
# x = Counter(str1)
# x.update("pppppppppp")
# print(x) # Counter({'p': 10, 'b': 3, 'i': 3, 'j': 3, 'g': 3, 't': 3, 'n': 2})
#
# # subtract 从一个可迭代对象中或者另一个映射（或counter）中，元素相减如果本来没有不会报错，而是显示-1
#
# y=Counter(list1)
# y.subtract([3,2])
# print(y)
# # {66: 1, 88: 1, 44: 1, 22: 4, 'a': 2, 'c': 1} # 原本的list1
# # {22: 4, 'a': 2, 66: 1, 88: 1, 44: 1, 'c': 1, 3: -1, 2: -1} # 变化后的list1
# '----------------------------------------------------------------'
# # 也可以做映射相减
# n_c = Counter(a = 4,b = 2,c = 0,d = -2)
# n_d = Counter(a = 1,b = 2,c = -3, d = 4)
# n_c.subtract(n_d)
# print(n_c) # Counter({'a': 3, 'c': 3, 'b': 0, 'd': -6})
#
# # 获取key和value
#
# print(list(Counter(str1).items())) # 字典的key和value
# print(list(Counter(str1).keys())) # 字典的key
# print(list(Counter(str1).values())) # 字典的value

'OrderedDict'
# 将有序字典传入然后进行操作
dict1 = {'a': 1,'b': 3, 'c':2}
od = collections.OrderedDict(dict1)
# od = collections.OrderedDict([('a', 1), ('z', 2), ('c', 3)])
# print (od)
# d = dict([('a',1),('z',2),('c',3)])
# print (d)

'defaultdict'
# Python中通过Key访问字典，当Key不存在时，会引发‘KeyError’异常。为了避免这种情况的发生，可以使用collections类中的defaultdict()方法来为字典提供默认值。
# from collections import defaultdict
# s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',5)]
# d = defaultdict(list)
# for k,v in s:
#     d[k].append(v)
# print(d.items())


'UserDict'


'UserList'


'UserString'




# 7.函数参数，返回值的软注释
# '''
# 为什么是软注释，因为注释后其实没有任何语法意义，只是为了规范，也不会影响性能
# 在声明变量时，变量的后面可以加一个冒号，后面再写上变量的类型，如 int、list 等等。
# 在声明方法返回值的时候,可以在方法的后面加一个箭头,后面加上返回值的类型，如 int、list 等等。
# '''
# from typing import List,Tuple,Dict,Any
#
# def Testa(a: int,b: str) -> List[int or str]:
#     list1 = []
#     list1.append(a)
#     list1.append(b)
#     return list1
# print(Testa.__annotations__) # 获取函数的注解
# print(Testa(166,'88'))
#
# def Testb(a:List[Any]) -> List[int or str]:
#     x = 10
#     y = range(x)
#     a.append(y)
#     return a
#
# list1 = [5]
# print(Testb.__annotations__)
# print(Testb(list1))


# 8. if not 语句
'''
if 条件语(判断为True则执行): 
    pass
if not 条件语(判断为False则执行):
    pass
    
在python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
'''

# a = [i for i in range(100) if not (i % 2) and (i % 3)]
# print(a)
#
# a = [2, 3, 4, 5, 6]
# for e in range(len(a)):
#     if not a[e] % 2 and a[e] % 3:  # not 后面的表达式为False才执行 同时被2，3整除后为0的数
#         print(a[e])
#
# if not {}:
#     print('1')

# 9. 上下文管理器 with语句
# 当实现了 __enter__ , __exit__ 两个魔法方法的类都可以用 with语句
# class TestWith(object):
#     def __enter__(self):
#         print("开始")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("结束")
# t = TestWith()
#
# with t:
#    print('中间运行')

#  10.for else语句
# for i in range(10):
#     print(i,end=" ")
# else:
#     print('代码运行结束')

# 11. round()
# '''
# 四舍五入规则：
#
# 要求保留位数的后一位<=4，则舍去3，如5.214保留小数点后两位，结果是5.21
# 要求保留位数的后一位“=5”，且该位数后面没有数字，则不进位，如5.215，结果为5.21
# 要求保留位数的最后一位“=5”，且该位数后面有数字，则进位，如5.2151，结果为5.22
# 要求保留位数的最后一位“>=6”，则进位。如5.216，结果为5.22
# '''
# print(round(1.15,1)) # 1.1
# print(round(1.151,1)) # 1.2
# print(round(2.675,2)) # 2.67
# print(round(2.6731,2)) # 2.67
# print(round(2.6751,2)) # 2.68

# # 12.retrying 模块 （重试函数）
# '''
#     def __init__(self,
#                  stop=None,
#                  wait=None,
#                  stop_max_attempt_number=None, # 设定最大的尝试次数，超过该次数就停止重试
#                  stop_max_delay=None, #  设置失败重试的最大时间, 单位毫秒，超出时间，则停止重试
#                  wait_fixed=None, # 两次调用方法期间停留时长
#                  wait_random_min=None,wait_random_max=None, # 设置失败重试随机性间隔时间（毫秒）
#                  wait_incrementing_start=None,
#                  wait_incrementing_increment=None, # 每调用一次则会增加的时长
#                  wait_exponential_multiplier=None, # 以指数的形式产生两次retrying之间的停留时间
#                  wait_exponential_max=None, # 最大间隔时间
#                  retry_on_exception=None, # 指定一个函数，如果此函数返回指定异常，则会重试，如果不是指定的异常则会退出
#                  retry_on_result=None, # 指定一个函数，如果指定的函数返回True，则重试，否则抛出异常退出
#                  wrap_exception=False,
#                  stop_func=None, # 每次抛出异常时都会执行的函数，
#                  wait_func=None,
#                  wait_jitter_max=None
#                  )
# '''
# from retrying import retry
# @retry(stop_max_attempt_number=5)  # 重试的次数
# def fun1():
#     print("this is func1")
#     raise ValueError
# try:
#     fun1()
# except ValueError:
#     print('ValueError')

# 13.ast(抽象语法树)Ast是python源码到字节码的一种中间产物
# import ast
# # eval 能将字符串变成原有的类型  literal_eval 也一样 但literal_eval 会安全很多
# str_list = '[1,2,3]'
# str_list_eval = eval(str_list)
# str_list_eval_1 = ast.literal_eval(str_list)
# print(str_list_eval,str_list_eval_1)

# 14. pickle 将对象简单存入文件
import pickle


# 15. issubclass,isinstance,hasattr
# issubclass()
# isinstance()
# hasattr(class,'name')

# 16 parse 再见re

# 17 匿名函数(lambda) 归约 (reduce) 过滤(filter)
# lambda params: expression 参数: 表达式

# 三目表达式
t = lambda x,y : x if x > y else y
# map 映射 map(func, iterable)
# list1 = [1,2,3,4,5,6]
# list2 = list(map(lambda x:x**2,list1))
# add = list(map(lambda x,y : x+y ,list1,list2))# [2, 6, 12, 20, 30, 42]

# reduce 归约 可以传参2个
from functools import reduce
# reduce(function, iterable[, initializer]) 最后那个是初始化参数 (多一个第一个数)
# res = reduce(lambda x, y: x + y, range(1,101)) # 5050
# res1 = reduce(lambda x, y : x + y, range(1,101), 100) # 5150
# list_str = ['1', '2', '3', '4']
# res2 = reduce(lambda x, y : x + y, list_str,'xyz') # xyz1234

# filter 过滤
# list_filter = [1,0,0,0,1]
# res_f = filter(lambda x: True if x == 1 else False, list_filter)
# print(list(res_f)) # [1, 1]

# sorted 排序

# 18. demjson
import demjson