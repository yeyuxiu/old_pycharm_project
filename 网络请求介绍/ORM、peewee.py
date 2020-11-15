# ORM、peewee
# ORM 对象映射处理
from peewee import *
db = MySQLDatabase('spider',host="127.0.0.1",port = 3306,user="root",password='123456')
# 一开始__init__的是数据库名，后面的密码要str

class BaseModel(Model):
    class Meta:
        database = db
class Person(BaseModel):
    name = CharField(max_length=20)
    # 如果没有primary_key标名，那么会自动增加id属性 也可以自己设计id
    birthday = DateField()

    # class Meta:
    #     database = db
    #     table_name = "users"
    #     如果不加table_name 会自动用类名 spider (小写)


if __name__ == "__main__":
    from datetime import date
    db.create_tables([Person])
    # 数据插入
    # test_save = Person(name='BO',birthday=date(1928,1,1))
    # test_save.save()


    # 查询数据 (只获取一条) get方法在娶不到数据会抛出异常 通常要 try
    # abc = Person.select().where(Person.name=='BO').get()
    # abc = Person.get(Person.name=='BO')
    #原生mysel语法 # " select * from person where name ='abc' "
    # print(abc.birthday)

    # 获取多条(取不到不会抛异常) 像一个列表，可以用分片，如果要从第二条开始取的话就在后面添加 [1:]
    # query = Person.select().where(Person.name=="BO")
    # for person in query:
    #     print(person.birthday,person.name)

    # 修改数据
    # query = Person.select().where(Person.name=="BO")
    # for person in query:
    #     person.birthday = date(1999,12,12)
    #     person.save()

    # 删除数据
    # query = Person.select().where(Person.name=="BO")
    # for person in query:
    #     person.delete_instance()
