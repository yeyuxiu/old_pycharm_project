# Scrapy 去重原理

# Scrapy telnet

'''
1. Scrapy的基础概念
2. 工作流程
3. 入门使用
4. 深入
5. Crawlerspider的使用
'''
# Scrapy的工程流程
'''
url队列 发送给 发送请求 然后 到 内容提取 数据队列 保存数据
Scher         Downloader     Spider   Itempipeline 
Scheduler 调度 存放url  Scheduler - > Downloader 有个中间件 下载中间件
Downloader 下载器 下载url 到 response Downloader -> SPider 有个 SpiderMiddlerware
SPiders 提取数据跟url地址返回给 Scheduler 和 ItemPipeline ( 其中url会组装成Request对昂给Scheduler )
ItemPipeline统一处理返回来的数据

'''
# 使用Pipeline
'''


'''

