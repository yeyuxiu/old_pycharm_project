'''
不可变数据类型在第一次声明赋值声明的时候, 会在内存中开辟一块空间, 用来存放这个变量被赋的值,
而这个变量实际上存储的, 并不是被赋予的这个值, 而是存放这个值所在空间的内存地址, 通过这个地址,
变量就可以在内存中取出数据了. 所谓不可变就是说, 我们不能改变这个数据在内存中的值,
所以当我们改变这个变量的赋值时, 只是在内存中重新开辟了一块空间,
将这一条新的数据存放在这一个新的内存地址里,
原来的那个变量就不在引用原数据的内存地址而转为引用新数据的内存地址了.
'''

# 总结：不可变数据类型更改后地址发生改变，可变数据类型更改地址不发生改变

# 不可变 : 整数 、 str 、 tuple(要对元组做限制，只能存放数字和字符串的不可变元素)
# a = 1
# print(id(a),type(a))
# a = 2
# print(id(a),type(a))
#
# str1 = 'ni'
# print(id(str1),type(str1))
# str1= 'nihao'
# print(id(str1),type(str1))

# # 元组被成为只读列表，数据可以被查询，但不能被修改
a = [1,2]
b = (a,3,4)
print(b,id(b),type(b))
a[0] = 'nihoa'
print(b,id(b),type(b))
print('虽然id没变，但元组本来就是不可变的，里面的列表是可变的，我们改变了列表')

# # 可变 : 列表 、 集合 、 字典
# s = {1,'d','34','1',1}
# print(s,type(s),id(s))
# s.add('djx')
# print(s,type(s),id(s))
#
# list = [1,'q','qwer',True]
# print(list,type(list),id(list))
# list.append('djx')
# print(list,type(list),id(list))
#
#
# d = {'key2':'djx','key3':'li'}
# print(d,type(d),id(d))
# d['key4'] = 'haha'
# print(d,type(d),id(d))

#  += 与 + 的区别
'''
a = 1
1 赋值给了 a 同时 a又指向了 1 这个对象
因为整数是不可变类型，所以 a = 2 时 id(a)改变
'''

'''
+= 操作首先会调用 __iadd__ 方法，如果没有则会调用__add__方法
__iadd__ : 接受两个参数，他会改变第一个参数的值(需要对象是可变的,所以对于不可变对象没有__iadd__这个方法)
__add__ : 接受两个参数，返回他们的和，两个参数的值均不变
'''
hasattr(int, '__iadd__')  #False
hasattr(list, '__iadd__') #True



print('list 拥有 __iadd__ 这个方法')
x = [1,2]
y = x
y += [3]
print(x,y)

print('+直接调用__add__这个方法，只改变+号的那个值')
x = [1,2]
y = x
y = y + [3]
print(x,y)
