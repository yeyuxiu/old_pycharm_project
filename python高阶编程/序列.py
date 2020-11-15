# list (什么都能存放) array (只能存放相同类型的元素，需要存放大量浮点数)
# deque (双向操作,需要频繁先进先出) bisect (只能存放升序列表，需要快速查找且顺序)
# 切片操作
# Lista = [1,2,3,4,5,6]
#
# Lista[:0] = ['a'] # 相当于 Lista += ['a']
# Lista[3:3] = [0] # 切换3的位置的元素
# Lista[:3] = [] # 删除操作
# del Lista[::2] # 隔开一个删一个0

import bisect # 二分查找
''' 
'bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right'
使用这些函数前要确保操作的列表是有序的。
'''
# 用来处理已排序的序列，用来维护已排序的序列，升序

# inter_list = [1,2,3,4,8,6,5]
# inter_list.sort()
# # insort(list,item) 把 item 插入到 升序的list中并保持升序
# bisect.insort(inter_list,7)
# # bisect (list,item) 查找要插入的 item 在 list中是什么位置，不插入只是返回位置
# bisect.bisect(inter_list,0)
# # bisect_left(list,item) 和 bisect_right(list,item)
# # 用于处理将要插入的重复数值的情况，返回将要插入的位置
# # bisect_left 若 item 存在时返回 item 左侧的位置
# # bisect_right 若 item 存在时返回 item 右侧的位置
# left = bisect.bisect_left(inter_list,4)
# right = bisect.bisect_right(inter_list,4)
# print(left,right)
# # insort_left(list,item) 和 insort_left(list,item)
# # insort_left item 存在时插入左侧 right右侧
# bisect.insort_left(inter_list,5)

# array , deque
import array



# deque
# from collections import deque
# my_deque = deque('123456789',maxlen=5)
# print(my_deque)
# my_deque.pop() # 9
# my_deque.popleft() # 1


# # 列表生成式
# list1 = [i*i for i in range(21) if i % 2 == 1]
# # 生成器表达式
# gen1 = (i*i for i in range(21) if i % 2 == 1)
# # 字典推导式
# dict1 = {"name":"yyx","name2":"nihao"}
# my_dict1 = {value:key for key,value in dict1.items()}
# # 集合推导式
# my_set = {key for key,value in dict1.items()}
# print(type(my_set))

# ---- dict 和 set 的实现原理和特性
# dict采用了哈希运算，所以查询时的复杂度为 O(1) 比遍历快，而且数据存入越多也不会改变他的查询时间
'''
1. dict的key 或 set 的 value 都必须是可hash的
2. 通常存入一些不可改变对象 str、fronzenset、tuple 自己定义的类如果返回__hash__则也是可以dict的
3. dict的内存花销大，但查询快
4. dict的存储顺序和元素添加顺序有关 (冲突)
5. 添加数据有可能改变已有数据的顺序
'''