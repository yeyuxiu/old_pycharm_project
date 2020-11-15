# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from ..items import PostMongoItem,AuthorMongoItem
import json,re
from urllib.parse import urljoin
import pymongo
from scrapy_redis.spiders import RedisSpider

class SpiderCsdnSpider(RedisSpider):
    name = 'spider_csdn'
    allowed_domains = ['bbs.csdn.net','me.csdn.net']
    base_url = "https://bbs.csdn.net/"
    redis_key = "spider_csdn:start_urls"
    # https://bbs.csdn.net/dynamic_js/left_menu.js?csdn
    # 获取左侧菜单所有url
    def parse(self, response):
        left_menu_data = re.findall(r"forumNodes:(.+])",response.text)
        json_all = json.loads(left_menu_data[0])
        left_url_list = []

        def get_children(json):
            for each_json in json:
                url = each_json.get('url')
                left_url_list.append(urljoin("https://bbs.csdn.net/", url))
                children = each_json.get("children")
                if children:
                    get_children(children)
        get_children(json_all)
        left_zongurl_list = []

        for each_json in json_all:
            if each_json.get('url'):
                left_zongurl_list.append(urljoin(self.base_url, each_json.get('url')))
        for each_zongurl in left_zongurl_list:
            if each_zongurl in left_url_list:
                left_url_list.remove(each_zongurl)
        left_url_list.remove(self.base_url)

        for each_left_url in left_url_list:
            yield Request(url=each_left_url,callback=self.parse_Getallwait)
            # yield Request(url=urljoin(each_left_url,'/recommend'),callback=self.parse_Getallrecommend)
            # yield Request(url=urljoin(each_left_url,'/closed'),callback=self.parse_Getallclosed)

    # 帖子详情内容
    def parse_post_detail(self,response):
        item = response.meta['item']
        close_title = response.xpath("//div[@class='user_right']/div[@class='close_topic']/text()").get().replace(' ', '')
        close_post = re.findall(r'(\d.+%|\d%)', str(close_title))[0]
        like = response.xpath(
            "//dd[@class='topic_r post_info floorOwner']//label[@class='red_praise digg d_hide']/em/text()").get()

        like_nums = re.findall(r'(\d.+|\d)', str(like))
        if like_nums:
            item['like_nums'] = int(like_nums[0])
        else:
            item['like_nums'] = 0
        item['close_post'] = close_post
        yield item

    # 作者页获取
    def parse_author(self,response):
        item = AuthorMongoItem()
        author_name = response.meta['author_name']
        # 检测作者是否重复
        global author_coll
        client = pymongo.MongoClient(host='localhost', port=27017)
        if "CSDN" in client.list_database_names():
            db = client['CSDN']  # 等价于 client.test #蓝色的叫数据库 黄色叫列表
            author_coll = db.author  # 增
        else:
            pass
        if not author_coll.find_one({"author_name":author_name}):
            rangking = response.xpath(
                "//div[@class='me_chanel_det']/div[@class='me_chanel_det_item access'][2]/span/text()").get().replace(
                " ", '').strip()
            # int
            article_nums = response.xpath(
                "//div[@class='me_chanel_det']/div[@class='me_chanel_det_item access'][1]/a/span/text()").get().replace(
                " ", '').strip()
            # int
            fans_nums = response.xpath("//div[@class='me_fans clearfix']/div[@class='fans']/a/span/text()").get().replace(
                " ", '').strip()
            # int
            attention_nums = response.xpath(
                "//div[@class='me_fans clearfix']/div[@class='att']/a/span/text()").get().replace(" ", '').strip()
            item['author_name'] =author_name
            item['rangking'] =rangking
            item['article_nums'] =int(article_nums)
            item['fans_nums'] =int(fans_nums)
            item['attention_nums'] =int(attention_nums)
            yield item

    def parse_Getallwait(self,response):
        global title_id, check_nums, lately_answer_time, create_time, answer_nums, author_url
        author_base_url = "https://me.csdn.net/"
        for each_tr in response.xpath("//div[@class='forums_table_c']//tbody/tr"):
            item = PostMongoItem()
            # # 置顶
            zhiding = each_tr.xpath("td[@class='forums_topic']/span[@class='green']/text()").get()
            if zhiding:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get():
                    title_id = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[2]/text()").get()
            else:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get():
                    title_id = \
                    each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get():
                author_url = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get().split("/")[-1]

            post_statue = each_tr.xpath(
                "td[@class='forums_topic_flag']/span[@class='topic_flag topic_flag_3']/text()").get()
            reward = each_tr.xpath("td[@class='forums_score']/em[@class='gain_score']/text()").get()
            create_author = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/text()").get()
            lately_author = each_tr.xpath("td[@class='forums_last_pub']/a[@class='Hash']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/em/text()").get():
                create_time = each_tr.xpath("td[@class='forums_author']/em/text()").get().split(' ')[0]
            if each_tr.xpath("td[@class='forums_last_pub']/em/text()").get():
                lately_answer_time = each_tr.xpath("td[@class='forums_last_pub']/em/text()").get().split(' ')[0]

            # 回复查看放在一起
            if each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get():
                checkoranswer = each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get().split(
                    '/')
                check_nums = checkoranswer[1]
                answer_nums = checkoranswer[0]
            # 帖子id
            item['title_id'] = int(title_id)
            # 帖子主题
            item['post_title'] = post_title
            # 帖子状态
            item['post_statue'] = post_statue
            # 赏分
            item['reward'] = int(reward)
            # 查看数
            item['check_nums'] = int(check_nums)
            # 最后回复时间
            item['lately_answer_time'] = lately_answer_time
            # 创作作者名
            item['create_author'] = create_author
            # 最后回复作者名
            item['lately_author'] = lately_author
            # 创贴时间
            item['create_time'] = create_time
            # 回复数
            item['answer_nums'] = int(answer_nums)
            # 作者url
            item['author_url'] = urljoin(author_base_url, author_url)
            # 帖子url
            item['post_url'] = urljoin(self.base_url,post_url)

            yield Request(url=urljoin(author_base_url, author_url), callback=self.parse_author,meta={'author_name':author_url})
            yield Request(url=urljoin(self.base_url,post_url), callback=self.parse_post_detail,meta={'item':item})
        # 获取下一页
        nextpage = response.xpath("//thead//div[@class='page_nav']/a[@class='pageliststy next_page'][1]/@href").get()
        if nextpage:
            next_page_url = urljoin(self.base_url, nextpage)
            yield Request(url=next_page_url,callback=self.parse_Getallwait)
    def parse_Getallrecommend(self,response):
        global title_id, check_nums, lately_answer_time, create_time, answer_nums, author_url
        author_base_url = "https://me.csdn.net/"
        for each_tr in response.xpath("//div[@class='forums_table_c']//tbody/tr"):
            item = PostMongoItem()
            # # 置顶
            zhiding = each_tr.xpath("td[@class='forums_topic']/span[@class='green']/text()").get()
            if zhiding:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get():
                    title_id = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[2]/text()").get()
            else:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get():
                    title_id = \
                        each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get():
                author_url = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get().split("/")[-1]

            post_statue = each_tr.xpath(
                "td[@class='forums_topic_flag']/span[@class='topic_flag topic_flag_3']/text()").get()
            reward = each_tr.xpath("td[@class='forums_score']/em[@class='gain_score']/text()").get()
            create_author = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/text()").get()
            lately_author = each_tr.xpath("td[@class='forums_last_pub']/a[@class='Hash']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/em/text()").get():
                create_time = each_tr.xpath("td[@class='forums_author']/em/text()").get().split(' ')[0]
            if each_tr.xpath("td[@class='forums_last_pub']/em/text()").get():
                lately_answer_time = each_tr.xpath("td[@class='forums_last_pub']/em/text()").get().split(' ')[0]

            # 回复查看放在一起
            if each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get():
                checkoranswer = each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get().split(
                    '/')
                check_nums = checkoranswer[1]
                answer_nums = checkoranswer[0]
            # 帖子id
            item['title_id'] = int(title_id)
            # 帖子主题
            item['post_title'] = post_title
            # 帖子状态
            item['post_statue'] = post_statue
            # 赏分
            item['reward'] = int(reward)
            # 查看数
            item['check_nums'] = int(check_nums)
            # 最后回复时间
            item['lately_answer_time'] = lately_answer_time
            # 创作作者名
            item['create_author'] = create_author
            # 最后回复作者名
            item['lately_author'] = lately_author
            # 创贴时间
            item['create_time'] = create_time
            # 回复数
            item['answer_nums'] = int(answer_nums)
            # 作者url
            item['author_url'] = author_url
            # 帖子url
            item['post_url'] = post_url
            yield item
            yield Request(url=urljoin(author_base_url, author_url), callback=self.parse_author,meta={'author_name':author_url})
            yield Request(url=urljoin(self.base_url, post_url), callback=self.parse_post_detail,meta={'item':item})
        # 获取下一页
        nextpage = response.xpath("//thead//div[@class='page_nav']/a[@class='pageliststy next_page'][1]/@href").get()
        if nextpage:
            next_page_url = urljoin(self.base_url, nextpage)
            yield Request(url=next_page_url, callback=self.parse_Getallrecommend)
    def parse_Getallclosed(self,response):
        global title_id, check_nums, lately_answer_time, create_time, answer_nums, author_url
        author_base_url = "https://me.csdn.net/"
        for each_tr in response.xpath("//div[@class='forums_table_c']//tbody/tr"):
            item = PostMongoItem()
            # # 置顶
            zhiding = each_tr.xpath("td[@class='forums_topic']/span[@class='green']/text()").get()
            if zhiding:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get():
                    title_id = each_tr.xpath("td[@class='forums_topic']/a[2]/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[2]/text()").get()
            else:
                post_url = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get()
                if each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get():
                    title_id = \
                        each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/@href").get().split("/")[-1]
                post_title = each_tr.xpath("td[@class='forums_topic']/a[@class='forums_title ']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get():
                author_url = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/@href").get().split("/")[-1]

            post_statue = each_tr.xpath(
                "td[@class='forums_topic_flag']/span[@class='topic_flag topic_flag_3']/text()").get()
            reward = each_tr.xpath("td[@class='forums_score']/em[@class='gain_score']/text()").get()
            create_author = each_tr.xpath("td[@class='forums_author']/a[@class='Hash']/text()").get()
            lately_author = each_tr.xpath("td[@class='forums_last_pub']/a[@class='Hash']/text()").get()
            if each_tr.xpath("td[@class='forums_author']/em/text()").get():
                create_time = each_tr.xpath("td[@class='forums_author']/em/text()").get().split(' ')[0]
            if each_tr.xpath("td[@class='forums_last_pub']/em/text()").get():
                lately_answer_time = each_tr.xpath("td[@class='forums_last_pub']/em/text()").get().split(' ')[0]

            # 回复查看放在一起
            if each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get():
                checkoranswer = each_tr.xpath("td[@class='forums_reply']/span[@class='reply_num']/text()").get().split(
                    '/')
                check_nums = checkoranswer[1]
                answer_nums = checkoranswer[0]
            # 帖子id
            item['title_id'] = int(title_id)
            # 帖子主题
            item['post_title'] = post_title
            # 帖子状态
            item['post_statue'] = post_statue
            # 赏分
            item['reward'] = int(reward)
            # 查看数
            item['check_nums'] = int(check_nums)
            # 最后回复时间
            item['lately_answer_time'] = lately_answer_time
            # 创作作者名
            item['create_author'] = create_author
            # 最后回复作者名
            item['lately_author'] = lately_author
            # 创贴时间
            item['create_time'] = create_time
            # 回复数
            item['answer_nums'] = int(answer_nums)
            # 作者url
            item['author_url'] = author_url
            # 帖子url
            item['post_url'] = post_url
            yield item
            yield Request(url=urljoin(author_base_url, author_url), callback=self.parse_author,meta={'author_name':author_url})
            yield Request(url=urljoin(self.base_url, post_url), callback=self.parse_post_detail,meta={'item':item})
        # 获取下一页
        nextpage = response.xpath("//thead//div[@class='page_nav']/a[@class='pageliststy next_page'][1]/@href").get()
        if nextpage:
            next_page_url = urljoin(self.base_url, nextpage)
            yield Request(url=next_page_url, callback=self.parse_Getallclosed)
