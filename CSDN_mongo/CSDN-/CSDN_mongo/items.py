# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item

class PostMongoItem(Item):

    # 帖子id
    title_id = Field()
    # 帖子主题
    post_title = Field()
    # 帖子状态
    post_statue = Field()
    # 赏分
    reward = Field()
    # 查看数
    check_nums = Field()
    # 最后回复时间
    lately_answer_time = Field()
    # 点赞数
    like_nums = Field()
    # 创作作者名
    create_author = Field()
    # 最后回复作者名
    lately_author = Field()
    # 创贴时间
    create_time = Field()
    # 回复数
    answer_nums = Field()
    # 结帖率
    close_post = Field()
    # 作者url
    author_url = Field()
    # 帖子url
    post_url = Field()

class AuthorMongoItem(Item):
    _id = Field()
    # 作者名
    author_name = Field()
    # 博文数
    article_nums = Field()
    # 排名
    rangking = Field()
    # 他的粉丝
    fans_nums = Field()
    # 他的关注
    attention_nums = Field()