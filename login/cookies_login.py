import time
import requests
from selenium import webdriver
import json


driver_c_l = webdriver.Chrome()
driver_c_l.maximize_window()
#file path needs change
file = open("get_cookies.json")
t = json.load(file)

url = t['link']
driver_c_l.get(url)
#file path needs change
with open('cookies'+t['name']+'.json','r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)

    # 方法1 将expiry类型变为int
    for cookie in cookies_list:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver_c_l.add_cookie(cookie)

time.sleep(4)


