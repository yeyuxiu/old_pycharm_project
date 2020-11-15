
import asyncio

from pyppeteer import launch


async def main():
    # 浏览器 启动参数
    start_parm = {
        # 关闭无头浏览器 默认是无头启动的
        "headless": False,
    }
    # 创建浏览器对象，可以传入 字典形式参数
    browser = await launch(**start_parm)

    # 创建一个页面对象， 页面操作在该对象上执行
    page = await browser.newPage()

    await page.goto('https://www.httpbin.org/headers')  # 页面跳转
    page_text = await page.content()  # 页面内容
    print(page_text)
    input('==========')
    await browser.close()  # 关闭浏览器对象


# asyncio.get_event_loop().run_until_complete(main())   # 创建异步池并执行main函数

async def resp_text():
    browser = await launch(headers=False)
    page = await browser.newPage()
    await page.goto('http://httpbin.org/headers')
    page_text = await page.content()
    print(page_text)
    await browser.close()

asyncio.get_event_loop().run_until_complete(resp_text())