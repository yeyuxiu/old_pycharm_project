# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DyItem
from scrapy.loader import ItemLoader

class TestCrawlSpider(CrawlSpider):
    name = 'test_crawl'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'),follow=True),
        Rule(LinkExtractor(allow=r'/zhaopin.*'),follow=True),
        Rule(LinkExtractor(allow=r'/jobs/\d.+'),callback = 'parse_tags',follow=True)
    )
    # 不同spider设置不同setting
    # custom_settings = {
    #    " COOKIES_ENABLED" : False,
    # }

    def parse_tags(self, response):
        # l = {}
        # return l
        l = ItemLoader(item = DyItem(),response =response)
        l.add_xpath('jobs_name','/html/body/div[7]/div/div[1]/div/h4')
        # for each_span in response.xpath("/html/body/div[7]/div/div[1]/dd/h3"):
        #     l.add_xpath('jobs_text','span/text()')
        yield l.load_item()


