# 面向对象语言的三大特性 : 封装、继承、多态
# ----多态----
# class A(object):
#     def move(self):
#         print("A moving")
# class B(object):
#     def move(self):
#         print("B moving")
# class C(object):
#     def move(self):
#         print("C moving")
# '''
# 调用相同的方法，对象不同得到的结果不同这就是多态，
# '''
#
# def move(obj):
#     obj.move()
#
# move(A())
# move(B())
# move(C())
# '''
# A moving
# B moving
# C moving
# '''


# ----鸭子类型----
# python 采用了鸭子类型(一个对象实现了__getitem__方法，我们就可以在他的基础上使用集合的方法)
# 不管传进来的是什么类型，只要是集合类型，那么就可以使用切片
# class DuckTest(object):
#     def __getitem__(self, item):
#         return item
# d = DuckTest()
# D = d.__getitem__([_ for _ in range(1, 5)])
# print(D[::-1])
# print(type('a',(object,),{'a':1}))

# python 一切皆对象 变量即对象 使得代码更加灵活方便
a = '123'
# a的类型:<class 'str'> str的类型:<class 'type'> type的类型:<class 'type'>
# type->class->str/int/list->实例
# type(name, bases, dict)
# print(type.__class__) # <class 'type'>
# print(type.__base__) # <class 'object'>  # 查看父类是什么
# print(object.__class__) # <class 'type'> # 查看对象是谁创建的
# ---- Class and Object ----
# Python 的自省机制 能够利用函数检测对象的属性与类型
# class Zixing(object):
#     def test_zixing(self):
#         return 1
#     def zixing_test(self):
#         return 2
# z = Zixing()
# print(type(z))
# print(dir(z))
# print(hasattr(z,'test_zixing'))
# print(isinstance(z,str))

# ---- isinstance 和  type 的区别
# class A(object):
#     pass
# class B(A):
#     pass
# b = B()
# print(type(b) is B)
# print(isinstance(b,B))
# print(type(b) is A)    # 采用type 去判断类型时，不会直接向上寻找父类，存在一定的偏差
# print(isinstance(b, A)) # isinstance 则会自动往上寻找

# ---- 静态方法 和 类方法 ----
# 静态方法是一类特殊的方法。有时，我们需要写属于一个类的方法，但是不需要用到对象本身
# 静态方法 跟 普通的def 差不多 但是进入到了类中，所以调用时要添加类名
# class Test_static(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     # 静态方法
#     @staticmethod
#     def add_stact(x,y):
#        print(x+1,y+1)
#     # 实例方法
#     def add(self):
#         return self.x,self.y
# s = Test_static(1,2)
#
# # 我们需要这么做才能+1
# s.x = s.x+1
# s.y = s.y+1
# print(s.add())
# # 采用了静态方法可以直接调用 不用每次实例化的时候都要写一次+1 才能完成步骤
# s.add_stact(1,2)

# 类方法
# 绑定在类上的方法 而非绑定在对象上
class Test_Classmethod(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @staticmethod
    def add(x,y):
        return Test_Classmethod(x+1,y+1) # 如果类名改了 那么静态方法中的类名也要跟着修改 ，类方法就为我们改善了这一弊端
    @classmethod
    def add_c(cls,x,y):
        return cls(
            x = x+1,
            y = y+1
        )
    def __str__(self):
        return "{x},{y}".format(x = self.x,y = self.y)

c = Test_Classmethod(1,2)
print(c.add(1,2))
print(c.add_c(1,2))

# super() 函数 关注顺序
# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     def __init__(self):
#         print("B")
#         super().__init__()
# class C(A):
#     def __init__(self):
#         print("C")
#         super().__init__()
# class D(B,C):
#     def __init__(self):
#         print("D")
#         super().__init__()
# if __name__ =="__main__":
#     print(D.__mro__)
#     d = D()


# with 语句的本质
# class Test_With(object):
#     def __enter__(self):
#         print('start')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
# #能够运行以下代码，也同时说明了 with语句其实就是 开始必须会执行跟结束必须会执行
# with Test_With() as t:
#     t