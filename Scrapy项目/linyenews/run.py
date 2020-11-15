
import os
import sys
# BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# print(BASE_DIR)
# sys.path.insert(0, os.path.join(BASE_DIR, 'ItemLoader CrawlSpider 用法'))
# insert 将路径加入到python path当中 就可以直接import

from scrapy.cmdline import execute
execute(["scrapy", "crawl", "news_spider"])






