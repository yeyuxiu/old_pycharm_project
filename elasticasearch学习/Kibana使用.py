# kibana的使用 端口 在cmd查看
''
'''
PUT csdn
{
  "settings": {
    "index" : {
      "number_of_shards":5,
      "number_of_replicas":1
    }
  }
}

# 查询settings信息
GET csdn/_settings
GET _all/_settings
GET .kibana,csdn/_settings
GET _settings

# 修改settings
PUT csdn/_settings
{
  "number_of_replicas": 2
}
# 获取索引信息
GET _all
GET csdn

# 保存文档
PUT csdn/_doc/1
{
  "title":"如何使用elasticsearch",
  "author":"叶毓琇",
  "check_like":{
    "check_nums":12,
    "like_nums":13
  },
  "create_data":"2020-8-4"
}

POST csdn/_doc/
{
  "title":"使用elasticsearch",
  "author":"叶琇",
  "check_like":{
    "check_nums":1,
    "like_nums":1
  },
  "create_data":"2020-8-4"
}

# 获取文章
GET csdn/_doc/1

GET csdn/_doc/1?_source=title,author
GET csdn/_doc/1?_source

# 修改文章(完全覆盖)
PUT csdn/_doc/1
{
  "title":"如何修改"
}

# 修改 增量覆盖
POST csdn/_update/1/
{
  "doc":{
    "company":20
  }
}

# 删除
DELETE csdn/_doc/1
# 删除type
DELETE csdn
'''
# 批量操作
'''
# 批量传入
GET csdn/_mget
{
  "docs":[
    {
      "_id":1
    }
    ]
}

GET csdn/_mget
{
  "ids":["1","jiiiVnQBJNuCsjNf4Nw5"]
}
# 批量传入数据
POST _bulk
{"index":{"_index":"csdn","_id":"454"}}
{"title":"h年后","name":"叶fgdc毓","data":"2020-8h-8"}
{"index":{"_index":"csdn","_id":"457"}}
{"title":"年fgh后","name":"叶fgdc毓","data":"2020-8h-8"}

# _bulk格式(一行指明命令一行实际数据)
{"indix":{"_index":"csdn","_id":"1"}}
{"field1":"value1"}
{"delete":{"_index":"csdn","_id":"1"}} # 只有一行
{"create":{"_index":"csdn","_id":"3"}}
{"field1":"value3"}
{"update":{"_id":"1","_indix":"csdn"}}
{"doc":{"file1":"value"}}
{}
'''