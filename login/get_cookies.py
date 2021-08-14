from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.webdriver import WebDriver

# 需要修改网站名和网站连接
file = open("get_cookies.json")
t = json.load(file)


def get_cookies(web):
    driver: WebDriver = webdriver.Chrome()
    driver.get(web)
    # 程序打开网页后*秒内 “手动登陆账户”
    time.sleep(20)
    with open('login_cookies/cookies' + t['name'] + '.json', 'w') as f:
        f.write(json.dumps(driver.get_cookies()))
    driver.quit()


get_cookies(t['link'])
