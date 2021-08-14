from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.webdriver import WebDriver

# json文件里有IP、账号、密码
file = open("get_cookies.json")
t = json.load(file)

"""
#代理IP
import urllib.request
proxy_support = urllib.request.ProxyHandler({'http': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

a = urllib.request.urlopen("https://www.baidu.com")
print(a.read())
"""


def get_cookies(web):
    driver: WebDriver = webdriver.Chrome()
    driver.get(web)
    # 程序打开网页后*秒内 “手动登陆账户”
    time.sleep(20)
    with open('login_cookies/cookies' + t['name'] + '.json', 'w') as f:
        f.write(json.dumps(driver.get_cookies()))
    driver.quit()


get_cookies(t['link'])
