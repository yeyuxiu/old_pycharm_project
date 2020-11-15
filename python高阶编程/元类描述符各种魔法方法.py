# 元类
'''
元类就是创建类的类， 对象 <- class(对象) <- type
python中类的实例化过程,会首先寻找,metaclass,通过metaclass去创建user类
metaclass优先级高
运用场景 : 可以做检查，实例化类的时候看看是否有某个方法


'''
# 经典类与新式类
'''
py2.x 经典类 深度优先
经典类的深度优先，子类继承多个父类的时候，如果继承的多个类中有属性相同的，那么排在第一的父类的属性会覆盖后面继承的类的属性，也就是如果集成的多个父类属性相同，那么以继承的第一个父类的属性为主;
py 3.x 广度优先
新式类的广度优先算法：子类继承多个父类的时候，如果继承的多个父类中有属性相同的，那么越往后继承的类将会覆盖前面的类的属性，也就是后来的继承的覆盖前面的；真正发挥了长江后浪推前浪的传统）
新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中。
新式类增加了__getattribute__方法
新式类内置有__new__方法而经典类没有__new__方法而只有__init__方法
'''

# 描述符
class IntField:
    def __get__(self, instance, owner):
        pass
    def __del__(self):
        pass
    def __set__(self, instance, value):
        pass

class NoneDataIntField:
    def __get__(self, instance, owner):
       return self.value
class User:
    age = IntField()
'''
把至少实现了内置属性 __set__() 和 __get__()方法的描述符称为数据描述符；
把实现__get__() 或者 __del__() 的方法的描述符称为非数据描述符;
'''

# 属性查找过程
'''
(1) 如果"age"是出现在User或者其基类__dict__中，且age是 数据描述符 ,那么会调用其__get__方法 (类中属性)
(2) 如果"age"出现在user对象的__dict__中，那么直接返回user.__dict__['age'], (对象中属性)
(3) 如果"age"出现在User或其基类的__dict__中 ( age = 1 )
(3.1) 如果age是 非数据描述符 那么会调用其__get__方法,否则返回 __dict__['age']
(4) 如果 User 有__getattr__方法， 调用 __getattr__方法，否则抛出AttributeError
'''

# property() 描述符 与 @property 装饰器

# property() 它的作用把方法当作属性来访问，从而提供更加友好访问方式。
# 描述符就是将某种特殊类型的类的实例指派给另一个类的属性
# 使得方法可以以属性的形式被访问和调用

class MyDecriptor:
    def __get__(self, instance, owner):
        '''
        :param self : MyDecriptor 类本身的实例
        :param instance: 拥有 MyDecriptor 的类的实例
        :param owner: 拥有者这个类本身
        '''
        print("getting...",self,instance,owner)
    def __set__(self, instance, value):
        '''
        :param value: 设置的值
        '''
        print("setting",self,instance,value)
    def __delete__(self,instance):
        print("deleting...",self,instance)


class Test:
    x = MyDecriptor()


''' @property
@property 语法糖提供了比 property() 函数更简洁直观的写法。
被 @property 装饰的方法是获取属性值的方法，被装饰方法的名字会被用做 属性名。
被 @属性名.setter 装饰的方法是设置属性值的方法。
被 @属性名.deleter 装饰的方法是删除属性值的方法。
### 一般会在对象属性名前加一个下划线 _ 避免重名，并且表明这是一个受保护的属性 ###
'''
# class Student:
#     def __init__(self):
#         self._age = None
#
#     @property
#     def age(self):
#         print('获取属性时执行的代码')
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         print('设置属性时执行的代码')
#         self._age = age
#
#     @age.deleter
#     def age(self):
#         print('删除属性时执行的代码')
#         del self._age
#
# student = Student()
# student.age = 18
# print('学生年龄为：' + str(student.age))
# del student.age

# 函数装饰器 : 有参和无参两种 (实现原理 : 函数嵌套+闭包+函数对象的组合使用产物)
# 让其他函数在不需要做任何代码变动的前提下增加额外功能
# 装饰器就是一个用来返回函数的函数


# __new__ 和 __init__ 的区别
'''
__new__ : 用来控制对象生成过程,是在生成对象之前就会调用（可以分别debug两个a）任务就是创建实例然后返回该实例对象，是个静态方法。
__init__ : 是当实例对象创建完成后被调用的,然后设置对象属性的一些初始值,产生对象后(a = A())被调用，
如果__new__ 方法不返回对象则不会调用 __init__
'''
# class A(object):
#     def __new__(cls, *args, **kwargs):
#         print("in new")
#         return super.__new__(cls)   # 返回实例化后的实例 传递给 __init__的 self (必须要return)
#     def __init__(self,name):
#         print("in init")
#         self.name = name
#
# a = A('nihao')
# # a = A(name = 'nihao')
# print(a)
'''
class display(object):
    def __init__(self, *args, **kwargs):
        print("init")
    def __new__(cls, *args, **kwargs):
        print("new")
        print(type(cls))
        return object.__new__(cls)
a=display()

在实例创建过程中__new__方法先于__init__方法被调用，它的第一个参数类型为type。
如果不需要其它特殊的处理，可以使用object的__new__方法来得到创建的实例（也即self)。
于是我们可以发现，实际上可以使用其它类的__new__方法类得到这个实例，只要那个类或其父类或祖先有__new__方法。
'''

class A(object):
    def __new__(cls,*args,**kwargs):
        print("Anew")
        return super().__new__(cls)
    def __init__(self,*args,**kwargs):
        print("Ainit")
'''       
class B(object):
    def __init__(self,*args,**kwargs):
        print("Binit")
    def __new__(cls,*args,**kwargs):
        print("Bnew")
        print(type(cls))
        return A.__new__(cls)
'''
#b=B()
a = A()
'''
newdis
<class 'type'>
newano
init
__init__提供生产的原料self(但并不保证这个原料来源正宗，
像上面那样它用的是另一个不相关的类的__new__方法类得到这个实例)，
而__init__就用__new__给的原料来完善这个对象（尽管它不知道这些原料是不是正宗的）
'''
