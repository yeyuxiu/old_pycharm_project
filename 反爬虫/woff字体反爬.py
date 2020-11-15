'''
TTFont用法
生成器简化操作用法
'''

import requests, re
from parsel import Selector
from urllib import parse
from fontTools.ttLib import TTFont
import hashlib

url = "http://www.porters.vip/confusion/movie.html"
resp = requests.get(url)
sel = Selector(resp.text)
# css(link[rel="stylesheet"]::attr(href))
css_path = sel.xpath('//link[@rel="stylesheet"]/@href').getall()
woffs = []

# 拼接正确的css文件路径
css_url = parse.urljoin(url, css_path[1])

# 向css文件发起请求
css_resp = requests.get(css_url)
# 匹配css文件中的woff文件路径
# src:url('../font/movie.woff') format('woff');
woff_path = re.findall(r"src:url\('..(.+\.woff)'\) format\('woff'\);", css_resp.text)
if woff_path:
    woffs += woff_path
woff_url = "http://www.porters.vip/confusion" + woffs.pop()

woff = requests.get(woff_url)
filename = "target.woff"
with open(filename, 'wb') as f:
    f.write(woff.content)
font = TTFont(filename)
web_code = '&#xe624.&#xe9c7'
###############################################################
woff_code = [i.upper().replace('&#X ', 'uni') for i in web_code.split('.')]
web_numdata = {}

num_name = font.getGlyphNames()
num_name.pop(0)
num_name.pop(10)
font1 = []

for i in num_name:
    # 获取字形信息数据
    content = font['glyf'].glyphs.get(i).data
    glyph = hashlib.md5(content).hexdigest()
    web_numdata['name'] = i
    web_numdata['hex'] = glyph
    font1.append(web_numdata)









