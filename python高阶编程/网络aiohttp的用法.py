import asyncio
import aiohttp
import requests

async def request():
    async with aiohttp.ClientSession() as session:
        #得到CelientSession对象
        #aiohttp.ClientSession(cookies=cookies)
        url = "https://www.baidu.com"
        async with session.get(url) as response:
            #async with异步上下文管理器
            #session.get/post(url)得到ClientResponse对象
            #session.put#可以有data/delete/head/options/patch可以有data
            #session.get(url,params=params,data=data,headers=headers,proxy=proxy,timeout=60)
            #data 通常是上传文件之类， params通常是上传一个列表 aiohttp将自动以字节流的形式发送个服务器
            
            print(response.status)
            print(response.text())
            #如果是获取大量数据,考虑使用字节流(StreamResponse)
            #response.content.read(10) 字节流读取响应内容 #读取前10字节
            #response.json()返回json/.read()#适合读取图像，无法编码/.text(encoding='utf-8')
            #response.status 查看状态码/.headers 查看headers /.cookie 查看cookie
task = [asyncio.ensure_future(request()) for _ in range(5)]
loop= asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))


# aiohttp简单使用(配合asyncio模块)

async def fetch_async(url):
    print(url)
    async with aiohttp.request("GET",url) as r:
        response = await r.text(encoding='utf-8')
        print(response)

tasks = [fetch_async('https://www.baidu.com'),
         fetch_async('https://cn.bing.com/')]
event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()

# 发起一个session请求



async def fetch_async_session(url):
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())
            #因为获取响应内容是一个阻塞过程，所以可以用await切换协程

tasks = [fetch_async_session("https://www.baidu.com"),
         fetch_async_session("https://cn.bing.com/")]
event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()
