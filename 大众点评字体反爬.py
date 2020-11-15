from fake_useragent import UserAgent
import requests,random,re,json
from parsel import Selector
from urllib.parse import urljoin,urlencode
from pyppeteer import launch
'''
1. 电话号码有svg
2. 评论文字有svg

'''

url = "http://www.dianping.com/shop/G5EEMuVn8LPuIJj7/review_all"
ua = UserAgent()

def requests_text(url):
    ua = UserAgent()
    headers = {"User-Agent":ua.random,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'no-cache',
               'Connection': 'keep-alive',
               'Cookie': '__mta=188578071.1599031901070.1599031901070.1599031901077.2; fspop=test; cy=4; cye=guangzhou; _lxsdk_cuid=173bd9c64e4c8-0af59643f10f4f-f7d123e-144000-173bd9c64e4c8; _lxsdk=173bd9c64e4c8-0af59643f10f4f-f7d123e-144000-173bd9c64e4c8; _hc.v=97e63aa4-a582-0c22-a126-1616c3bbb288.1599027056; s_ViewType=10; ctu=4f7dcd171bc09a6343cb6047b27dc911c76e1f990c31e6086a4d5820307280f3; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1599031892; wed_user_path=6699|0; _dp.ac.v=afb729b3-1d14-475f-bb23-d5140ee59874; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1596632253,1599027056,1599047468,1599095974; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1599098381; _lxsdk_s=174518c271f-36a-920-5e4%7C%7C421',
               'Host': 'www.dianping.com',
               'Pragma': 'no-cache',
               }
    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200:
        return resp.text
    else:
        return "the status_code is not 200"

def getbasic_meg(resp_text):
    # done
    basic_se = Selector(resp_text)
    shop_name = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[1]/h1/text()').get()
    reviews = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/span[1]/text()').get()
    each_price = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/span[2]/text()').re(r'(\d.+)')[0]
    taste = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/span[3]/span[1]/text()').re(r'(\d.+)')[0]
    environment = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/span[3]/span[2]/text()').re(r'(\d.+)')[0]
    server = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/span[3]/span[3]/text()').re(r'(\d.+)')[0]
    start = basic_se.xpath('//*[@id="review-list"]/div[2]/div[1]/div[2]/div/div/span[1]/@class').re(r'star_(\d+)')[0]
    get_svg_url = 'https:'+basic_se.xpath('/html/head/link[4]/@href').get()
    return shop_name,reviews,each_price,taste,environment,server,start,get_svg_url

# def get_address(url):
def get_class_local(get_svg_url):
    headers = {"User-Agent":ua.random}
    local_text = requests.get(url=get_svg_url,headers=headers).text
    # with open('class_local','w') as f:
    #     f.write(local_text)
    # with open('class_local','r') as f:
    #     text = f.read()
    class_localtion_list = re.findall(r'\.(.+?){background:-(.+?)px -(.+?)px;}',local_text)
    background_image_url = re.findall(r'\[class\^="(.+)"\].+background-image: url\((.+s3plus.meituan.net.+\.svg)\)',local_text)

    background_image_url = [(each_url[0],'https:'+each_url[1]) for each_url in background_image_url]
    class_localtion_list = [(each_class_localtion[0],int(float(each_class_localtion[1])),int(float(each_class_localtion[2]))) for each_class_localtion in class_localtion_list]
    return class_localtion_list,background_image_url

resp_text = requests_text(url)
shop_name,reviews,each_price,taste,environment,server,start,get_svg_url = getbasic_meg(resp_text)
class_localtion_list,background_image_url = get_class_local(get_svg_url)
print(class_localtion_list,background_image_url)