# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .items import LinyenewsItem


class MongoPipeline(object):
    collection_name = 'linye_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.client]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item.__class__ == LinyenewsItem:
            self.db[self.collection_name].incert(dict(item))
            return item
