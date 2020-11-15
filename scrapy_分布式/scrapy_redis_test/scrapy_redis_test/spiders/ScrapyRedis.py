# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from urllib.parse import urljoin

from scrapy import Spider,Request
from ..items import ScrapyRedisTestItem
import json,re

class ScrapyRedisSpider(RedisSpider):
    name = 'ScrapyRedis'
    # allowed_domains = ['']
    redis_key = "ScrapyRedis:start_urls"
    # base_url = ""

    def parse(self,response):
        menu_url_list = response.xpath("//div[@class='container']/ul[@class='nav']/li[@id='menu-item'][position()>2]/a/@href").getall()
        for each_menu_url in menu_url_list:
            menu_url = urljoin(self.base_url,each_menu_url)
            yield Request(url=menu_url,callback=self.parse_each_album)

    def parse_each_album(self,response):
        each_album_url_list = response.xpath("//div[@class='content-wrap']/div[@class='content']/article[@class='excerpt excerpt-one']//h2/a/@href").getall()
        for each_album_url in each_album_url_list:
            each_url = urljoin(self.base_url,each_album_url)
            yield Request(url=each_url,callback=self.parse_detail_image)
        if response.xpath("//div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href").get():
            next_url = urljoin(self.base_url,response.xpath("//div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href").get())
            yield Request(url=next_url,callback=self.parse_each_album)


    def parse_detail_image(self, response):

        for each_a in response.xpath("//article[@class='article-content']/p[position()>2]"):
            item = ScrapyRedisTestItem()
            item['image_url'] = urljoin(self.base_url,each_a.xpath("img/@src").get())

            item['image_name'] = ''.join(each_a.xpath("img/@src").get().split('/')[3:])
            yield item

        if response.xpath("/html/body/div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href"):
            next_page_url = urljoin(response.url,response.xpath("/html/body/div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href").get())
            yield Request(url=next_page_url,callback=self.parse)