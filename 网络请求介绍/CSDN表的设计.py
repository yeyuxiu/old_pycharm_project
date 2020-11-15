from peewee import *

database = MySQLDatabase('spider',host='127.0.0.1',port=3306,user='root',password='123456')

class BaseModel(Model):
    class Meta:
        db = database
# 关注几个点
'''
char 类型，要设置最大长度
对于无法确定最大长度的字段，可以设置为Text
设计表的时候采集到的数据要尽量先做格式化处理
default 和 null = True 的处理，有时候获取不到值
'''
class Topic(BaseModel):
    title = CharField()
    content = TextField(default="") # 不限长度
    csdn_id = IntegerField(primary_key=True)
    author = CharField()
    create_time = DateTimeField()
    answer_nums = IntegerField(default =0)
