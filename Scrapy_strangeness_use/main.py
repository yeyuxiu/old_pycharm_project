'''
scrapy py文件启动
将路径加入到 python path当中

'''
from scrapy.cmdline import execute
# execute(["scrapy","crawl","test_crawl"])
execute(["scrapy","crawl","spider"])

import os
import sys

# BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# print(BASE_DIR)
# D:\A_pycharm项目

# sys.path.insert(0, os.path.join(BASE_DIR, 'ItemLoader CrawlSpider 用法'))
# insert 将路径加入到python path当中 就可以直接import


