from scrapy.cmdline import execute
for each_fi in range(1,4):
    execute(["scrapy","crawl","spider_csdn","-s","JOBDIR=crawls/stop-%s" % str(each_fi)])
# execute(["scrapy","crawl","spider_csdn"])
