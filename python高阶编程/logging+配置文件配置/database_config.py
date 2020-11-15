# -*- coding:utf-8 -*-
import pymysql
import configparser
# cf= configparser.ConfigParser()
# cf.read('database.conf',encoding='utf-8')
# conn = pymysql.connect(
#         host = cf.get('mysql', 'DB_HOST'),
#         user = cf.get('mysql', 'DB_USER'),
#         passwd = cf.get('mysql', 'DB_PWD'),
#         db = cf.get('mysql', 'DB_NAME'),
#         port = cf.getint('mysql', 'DB_PORT'),
#         charset= cf.get("mysql", 'CHARSET'),
#     )
# cur = conn.cursor()
# sql="""select * from status"""
# cur.execute(sql)
# data=cur.fetchall()
# print(data)
# conn.close()
# import redis
# import configparser
#
# cf = configparser.ConfigParser()
# cf.read('database.conf', encoding='utf-8')
# r1 = redis.Redis(
#     host=cf.get('redis', 'REDIS_HOST'),
#     port=cf.getint('redis', 'REDIS_PORT'),
#     password=cf.get('redis', 'REDIS_PWD'),
#     db=cf.getint('redis', 'REDIS_DBID'))
# r1.set('name2', 'Jacson2')
# print(r1.get('name2'))
# import pymongo
# cf = configparser.ConfigParser()
# cf.read('database.conf', encoding='utf-8')
# mongo_db = pymongo.MongoClient(
#     host=cf.get("MONGO","MONGO_HOST"),
#     port = cf.get("MONGO","MONGO_PORT"),
# )
# db = mongo_db[cf.get("MONGO","MONGO_DB")]
# collection = db[cf.get("MONGO","MONGO_COLLECTION")]