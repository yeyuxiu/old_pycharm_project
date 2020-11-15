# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from scrapy.loader import ItemLoader
from ..items import DyItem
import datetime

from urllib.parse import urljoin


class SpiderSpider(Spider):
    name = 'spider'
    allowed_domains = ['www.dygangs.com']
    #start_urls 为元组
    start_urls = ['http://www.dygangs.com/ys/']

    def parse(self, response):

        #跟print一个效果 专业一点
        '''
        self.log("movie_name: %s" % response.xpath('//div\
            [@class="co_content2"]/ul/a/text()').getall())
        '''

        #ItemLoader用法

        next_page = response.xpath('//td[@align="middle"]/a[last()-1]/@href').get()

        l = ItemLoader(item = DyItem(), response = response)

        for i in l.get_xpath('//td[@width="250"]/a/@href'):

            yield Request(url = str(i),callback = self.sec_parse)

        yield Request(url = next_page,callback=self.parse)

    def sec_parse(self,response):

        l = ItemLoader(item=DyItem(), response=response)
        l.add_xpath('movie_name','//div[@align="center"]/a/text()')
        l.add_value('last_updated', datetime.datetime.now())
        return l.load_item()

