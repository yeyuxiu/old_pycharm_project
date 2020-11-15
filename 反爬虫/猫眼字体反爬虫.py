from fontTools.ttLib import TTFont
from fake_useragent import UserAgent
import requests,random,json,re
# 加载字体文件：
# font = TTFont('1.woff')

# # 保存为xml文件：
# font.saveXML('1.xml')

# 获取各节点名称，返回为列表
# print(font.keys())  # ['GlyphOrder', 'head', 'hhea', 'maxp', 'OS/2', 'hmtx', 'cmap', 'loca', 'glyf', 'name', 'post', 'GSUB']

# # 获取getGlyphOrder节点的name值，返回为列表
# print(font.getGlyphOrder())  # ['glyph00000', 'x', 'uniF013', 'uniF4D4', 'uniEE40', 'uniF7E1', 'uniF34B', 'uniE1A0', 'uniF1BE', 'uniE91E', 'uniF16F', 'uniF724']
# print(font.getGlyphNames())  # ['glyph00000', 'uniE1A0', 'uniE91E', 'uniEE40', 'uniF013', 'uniF16F', 'uniF1BE', 'uniF34B', 'uniF4D4', 'uniF724', 'uniF7E1', 'x']
#
# # 获取cmap节点code与name值映射, 返回为字典
# print(font.getBestCmap())  # {120: 'x', 57760: 'uniE1A0', 59678: 'uniE91E', 60992: 'uniEE40', 61459: 'uniF013', 61807: 'uniF16F', 61886: 'uniF1BE', 62283: 'uniF34B', 62676: 'uniF4D4', 63268: 'uniF724', 63457: 'uniF7E1'}
#
# # 获取glyf节点TTGlyph字体xy坐标信息
# print(font['glyf']['uniE1A0'].coordinates)  # GlyphCoordinates([(50, 335),(50, 468),(76, 544),(95, 638),(148, 676),(202, 710),(282, 710),(402, 710),(459, 617),(487, 574),(504, 501),(520, 437),(519, 335),(520, 271),(508, 166),(494, 126),(466, 46),(362, -39),(282, -49),(176, -35),(115, 37),(43, 121),(43, 335),(135, 335),(135, 154),(177, 95),(229, 35),(282, 35),(343, 35),(385, 107),(428, 155),(428, 339),(428, 515),(385, 576),(344, 635),(286, 635),(218, 635),(179, 583),(135, 506)])
#
# # 获取glyf节点TTGlyph字体xMin,yMin,xMax,yMax坐标信息
# print(font['glyf']['uniE1A0'].xMin, font['glyf']['uniE1A0'].yMin,
#       font['glyf']['uniE1A0'].xMax, font['glyf']['uniE1A0'].yMax)  # 0 -49 521 711
# print(font.getGlyphOrder()[2:])
from parsel import Selector

ua = UserAgent()
url = "https://maoyan.com/films/1230199"
headers = {"User-Agent":ua.random,}
resp_text = requests.get(url=url,headers=headers).text
se = Selector(resp_text)

stonefont = se.xpath("//div[@class='movie-index-content box']/span[@class='stonefont']/text()").extract_first()
print(stonefont)
pass

s = ""