import aiohttp
url = "https://www.baidu.com"
# async with aiohttp.ClientSession() as session:
#     async with session.get(url) as resp:
#         result = await resp.text()

from aiohttp_requests import requests
resp = await requests.get(url)
result1 = await resp.text()
print(result1)