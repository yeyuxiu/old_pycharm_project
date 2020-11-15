# -*- coding: utf-8 -*-

# Scrapy settings for linyenews project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'linyenews'

SPIDER_MODULES = ['linyenews.spiders']
NEWSPIDER_MODULE = 'linyenews.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linyenews (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Connection':'keep-alive',
#     'Cookie':'dict%5Fcookieflag=1; _gscu_1959539731=00561544lybp7o15; _gscbrs_1959539731=1; Hm_lvt_f25ddc1aa666f0b3893d8fcd6fb4c570=1600561545; _pk_testcookie.10.9433=1; ASPSESSIONIDACSRSRAS=HFHBHNLCGEGKBDKKEPFOHKPA; CGISESSIONID=EZTLUZFKLKHNDXLD; _pk_ref.10.9433=%5B%22%22%2C%22%22%2C1600564465%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DLF0Tr3hx3MLXzYNkNH_JSRqMvGuJBQznLIHd-dWQX_phR02GAMaHBvht0OkAcv1m%26wd%3D%26eqid%3Dab13bd77000b6043000000065f66a187%22%5D; _pk_ses.10.9433=1; BotMitigationCookie_1969904701684545095="100962001600565643/ZuaWkAygEkLenKjg/kKIE4WnEE="; _gscs_1959539731=t00564779p1z4yb11|pv:8; _pk_id.10.9433=c3a53664ec3e693d.1600561545.2.1600565529.1600564465.; Hm_lpvt_f25ddc1aa666f0b3893d8fcd6fb4c570=1600565529',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'linyenews.middlewares.MongoSpiderMiddleware': 543,
#}
# MONGO_URI = 'localhost:27017'
# MONGO_DB = 'news'
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'linyenews.middlewares.LinyenewsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'linyenews.pipelines.MongoPipeline': 300,
#}
UA_TYPE = 'random'
MONGO_URI = 'localhost:27017'
MONGO_DB = 'news'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
