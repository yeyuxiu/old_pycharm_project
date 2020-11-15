'''
基于java开发 基于 RESTful web 接口 分布式全文搜索引擎
https://www.elastic.co/use-cases
官网
https://www.elastic.co/cn/
与数据库相比的搜索引擎的优点
无法打分 无分布式 无法解析搜索请求 效率低 分词
在某种情况下 elasticsearch 可以当 mongodb来使用
'''
# 几个概念
'''
1. 集群 ： 一个或者多个节点组织在一起
2. 节点 ： 一个节点是集群中的一个服务器，由一个名字来识别，默认名称是个随机的漫画角色名字
3. 分片 ： 将索引划分为多份的能力，允许水平分割和扩展份量，多个分片响应请求，提高性能和吞吐量
4. 副本 ： 创建分片的一份或者多分的能力，在一个节点失败其余节点可以顶上
'''
'''# HTTP方法有8中 elasticsearch 常用4中 GET POST PUT(向服务器传送的数据取代指定的文档的内容) DELETE
elasticsearch           mysql
index(索引)           数据库
type(类型)            表
documents(文档)       行
fields                列
'''
# 倒排索引
'''
利用记录的位置来确定 记录 打分 位置
需要解决的问题
1. 大小写转换问题
2. 词干抽取，looking 、look 为一个词
3. 分词 屏蔽系统 和 屏蔽、系统 的区分
4. 倒排索引文件过大 - 压缩编码
'''
# 映射(mapping)
'''
Elasticsearch会根据JSON源数据的基础类型猜测你想要的字段映射，将输入的数据转变成可搜索的索引项。
Mapping就是我们自己定义的字段的数据类型，同时告诉Elasticsearch如何索引数据以及是否可以呗搜索
作用: 会让索引建立的更加细致和完善
类型: 静态映射和动态映射
自己定义的内置类型
    string类型 : text, keyword(string 类型在es5剋是已经废弃)
    数据类型 : long, integer, short ,byte, double, float
    日期类型 : date
    bool类型 : boolean
    binary类型 : binary
    复杂类型 : object, nested
    geo类型 : geo-point, geo-shape
    专业类型 : ip, competion
    
'''
