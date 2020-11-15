import re

import requests
from fake_useragent import UserAgent
from parsel import Selector
import random

def request_test(url):
    ua = UserAgent()
    headers = {
        'User-Agent':ua.random,
        "Cookie":"BIDUPSID=BDC12FDAC660BD9B287A4E3EF3C1EFAB; PSTM=1600659005; BAIDUID=BDC12FDAC660BD9BAF86230308EC22A9:FG=1; BD_UPN=12314753; BDUSS=QyUEx3bG9vbExZcHNtOH5IOUVUNXpSQmZwcS1JYTQ1WWYwczlhc2ZIfnMtWk5mSVFBQUFBJCQAAAAAAAAAAAEAAAB~WKM1SnVzdF9UZWFtX09uZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOxsbF~sbGxfcW; BDUSS_BFESS=QyUEx3bG9vbExZcHNtOH5IOUVUNXpSQmZwcS1JYTQ1WWYwczlhc2ZIfnMtWk5mSVFBQUFBJCQAAAAAAAAAAAEAAAB~WKM1SnVzdF9UZWFtX09uZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOxsbF~sbGxfcW; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=c445Bs88s13cwVNKkMr1X33VN7OHb24lKyGFRucNtS9Hlw17Vb2TC0TCQ%2BuqBryZVgR2; BD_HOME=1; H_PS_PSSID=32810_1442_32844_32723_32230_7517_32117_26350_22159; sug=3; sugstore=0; ORIGIN=2; bdime=0",
    }

    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200 :
        return resp.text

    else:
        return "is not 200"

url = "https://www.baidu.com/home/pcweb/data/mancardwater?&id=2"
for i in range(10):
    text = request_test(url)
    # print(text)
    print(re.findall(r'title:(.+);pos:0', text))


