import pymongo
import pandas as pd

# 有些时候，我们可能需要存入不同的数据库中，而settings中只能设置一个数据库的资料，那么这时候我们就需要使用custom_settings参数来为每一个spider配置对应的pipeline。不过scrapy版本必须是1.1以上

class Test1(scrapy.Spider):
        name = "test1"
        custom_settings = {
            'ITEM_PIPELINES':{'xxxx.pipelines.TestPipeline1': 301},
    }
class Test2(scrapy.Spider):
        name = "test2"
        custom_settings = {
            'ITEM_PIPELINES':{'xxxx.pipelines.TestPipeline2': 302},
    }

# 但是在settings里面也要配置pipeline：
ITEM_PIPELINES = {
    'xxxx.pipelines.TestPipeline1': 301,
    'xxxx.pipelines.TestPipeline2': 302
}

# 多爬虫一次运行

import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider1(scrapy.Spider):
    # Your first spider definition



class MySpider2(scrapy.Spider):
    # Your second spider definition



process = CrawlerProcess()  # 初始化事件循环
process.crawl(MySpider1)  # 将爬虫类方式事件循环
process.crawl(MySpider2)  # 将爬虫类方式事件循环
process.start()  # the script will block here until all crawling jobs are finished

# scrapy 数据收集器
# 在spider中设置
# class spider(Spider)
#     handle_httpstatus_list = [404]
#     def __init__(self,)
#         self.fail_urls = []
#     def parse(self,repsonse):
#         if response.status == 404:
#             self.fail_urls.append(response.url)
#             self.crawler.stats.inc_calue("failed_url")



