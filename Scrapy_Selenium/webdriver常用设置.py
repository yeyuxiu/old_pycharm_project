'''
如果想selenium一步一步运行的话(每输入一次指令就运行一步的selenium)
在cmd中 ipthon 然后一步一步输入代码，最后在cmd中输入 %hist 打印刚刚输入的代码
'''

from selenium import webdriver
import time
# 设置Chromedriver不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_opt.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(executable_path='D:/大学/python/3.72/Scripts/chromedriver.exe',options=chrome_opt)
browser.get("https://www.csdn.net/")
time.sleep(3)
browser.quit()
# 设置无头浏览器
from selenium.webdriver.chrome.options import Options
# option = Options()
# option.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=option)
