# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import AuthorMongoItem,PostMongoItem
class AuthorMongoPipeline(object):
    author_collection = "author"

    def __init__(self,mongo_db,mongo_uri):
        self.mongo_db = mongo_db
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_db = crawler.settings.get("MONGO_DB"),
            mongo_uri = crawler.settings.get("MONGO_URI")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        if item.__class__ == AuthorMongoItem:
            self.db[self.author_collection].insert(dict(item))
        return item

class PostMongoPipeline(object):
    post_collection = "post"

    def __init__(self,mongo_db,mongo_uri):
        self.mongo_db = mongo_db
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_db = crawler.settings.get("MONGO_DB"),
            mongo_uri = crawler.settings.get("MONGO_URI")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item,PostMongoItem):
            self.db[self.post_collection].insert(dict(item))
        return item