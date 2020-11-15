# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import re,json
import scrapy
from parsel import Selector
from ..items import LinyenewsItem


class NewsSpiderSpider(Spider):
    name = 'news_spider'
    allowed_domains = ['lknet.ac.cn']
    # start_urls = ['http://web/']
    base_url = "http://www.lknet.ac.cn/"

    def start_requests(self):
        url = "http://www.lknet.ac.cn/page/framelimit.cbs?ResName=mrxw"
        formdata = {
            'Un':'chaopi',
            'Pw':'NCCYshen',
        }
        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):

        url = "http://www.lknet.ac.cn/page/Brw_Tmpl6_RecordList.cbs?ResName=mrxw"
        formdata = {
            'ResName':'mrxw',
        }
        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse_title)

    def parse_title(self, response):
        test = response.text
        form_all = re.findall(r'(<FORM name=form2.+</form></table><table.+class=bgcolor-fanye><tr>)',response.text)[0]
        html_form_all = "<html><head><title></title></head><body>" + form_all + "</body></html>"
        # 将获取的form重新组装成html 去se
        se_form_all = Selector(html_form_all)

        begin_test = response.xpath('//input[@name="begin"]/@value').getall()
        if len(begin_test) < 4:
            begin = begin_test[0]
        else:
            begin = begin_test[2]
        fidvalue = response.xpath('//input[@name="fldvalue"]/@value').get()


        data = se_form_all.xpath("//tr[@class='bgcolor-gailan']/td[2]/a/text()").getall()
        title = se_form_all.xpath("//tr[@class='bgcolor-gailan']/td[3]/a/text()").getall()
        url = se_form_all.xpath("//tr[@class='bgcolor-gailan']/td[3]/a/@href").getall()
        for each_url in url:
            base_url = "http://www.lknet.ac.cn/page/"
            new_url = base_url + each_url

            yield Request(url=new_url,callback = self.parse_detail_content)

        item = LinyenewsItem()
        for each in range(len(title)):

            item['title'] = title[each]
            item['data'] = data[each]
        # yield item

        url = "http://www.lknet.ac.cn/page/Brw_Tmpl6_RecordList.cbs"
        formdata = {
            'fldvalue':str(fidvalue),
            'ResName':'mrxw',
            'begin':str(begin)
        }

        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse_title)


    def parse_detail_content(self, response):
        re_content = re.findall(r"<font color=darkblue>(.+)</font>",response.text)
        # content = response.xpath('//font[@color="darkblue"]/text()').getall()

        item = LinyenewsItem()
        item['content'] = re_content[0]
        yield item
