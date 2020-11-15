import time

from selenium import webdriver
from scrapy.http import HtmlResponse
# 在MiddlePipeline中设置
class JSPageMiddleware(object):
    # 设定这个browser只属于这个类 就可以每个spider共用一个Chrome 但有个问题就是 Chrome不会关闭
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='D:/大学/python/3.72/Scripts/chromedriver.exe')
        super(JSPageMiddleware, self).__init__()
    # 通过Chome 请求动态网页
    def process_request(self, request, spider):

        if spider.name == "jobbole":

            self.browser.get(request.url)
            time.sleep(3)
            # 一旦遇到这个类 HtmlResponse Downloader不会下载而是返回给我们的spider
            return HtmlResponse(url=self.browser.current_url,
                                body=self.browser.page_source,
                                encoding='utf-8',request=request
                                )
# 解决上面Chrome无法自动关闭的问题
# 在spider中设置
import scrapy
from pydispatch import dispatcher
from scrapy import signals

class JobbleSPider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com']
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='D:/大学/python/3.72/Scripts/chromedriver.exe')
        super(JobbleSPider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    def spider_closed(self,spider):
        self.browser.close()

# 同时在middle中设置
class J1SPageMiddleware(object):
    # 通过Chome 请求动态网页
    def process_request(self, request, spider):
        # 这里的不是 self.browser 而是 spider.browser

        if spider.name == "jobbole":

            spider.browser.get(request.url)
            time.sleep(3)
            # 一旦遇到这个类 HtmlResponse Downloader不会下载而是返回给我们的spider
            return HtmlResponse(url=spider.browser.current_url,
                                body=spider.browser.page_source,
                                encoding='utf-8',request=request
                                )


