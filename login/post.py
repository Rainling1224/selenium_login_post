import time

import selenium
import pyautogui
from selenium import webdriver
import json
from cookies_login import driver_c_l
# 报错的原因是重名，修改为driver_c_l


# twitter不需要再一次刷新 driver.refresh()
def twitter_post():
    time.sleep(5)
    try:
        # 输入文本
        driver_c_l.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div') \
            .send_keys('test')
        # 点击发布
        driver_c_l.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]') \
            .click()
    except:
        print("error")


def youtube_post():
    try:
        driver_c_l.find_element_by_xpath().send_keys()
        driver_c_l.find_element_by_xpath().click()
    except:
        print("error")


def facebook_post():
    driver_c_l.refresh()
    time.sleep(5)
    try:
        driver_c_l.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div').click()
        time.sleep(3)# 弹出的窗口是div，不需要定位，但需要等待
        driver_c_l.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div').send_keys('hello')
        driver_c_l.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div').click()
    except:
        print("error")


def linkedin_post():
    driver_c_l.refresh()
    time.sleep(5)
    try:
        driver_c_l.find_element_by_id("ember65").click()
        time.sleep(3)
        driver_c_l.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p').send_keys('hello')
        time.sleep(3)
        driver_c_l.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button').click()
    except:
        print("error")


def vimeo_post():
    driver_c_l.refresh()
    time.sleep(5)
    try:
        driver_c_l.find_element_by_xpath('//*[@id="wrap"]/div[2]/main/div/div/div[1]/div[1]/div/div[1]/section[1]/button').click()
        time.sleep(3)
        driver_c_l.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div[1]/section[1]/div/div/div[1]/input').send_keys('E:\\video\\test.mp4')
        time.sleep(3)
    except:
        print("error")


def tiktok_post():
    driver_c_l.refresh()
    # 等待时间稍长，需要滑块验证
    time.sleep(20)
    try:
        driver_c_l.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div[1]').click()
        driver_c_l.implicitly_wait(10)
        driver_c_l.find_element_by_xpath(
            '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/input').send_keys('E:\\video\\test.mp4')
        driver_c_l.implicitly_wait(10)
        driver_c_l.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span').send_keys(
            'test')
        time.sleep(3)
        driver_c_l.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[6]/button[2]').click()
        time.sleep(3)
    except:
        print("error")


def pinterest_post():
    driver_c_l.refresh()
    time.sleep(5)
    try:
        # 有时会报错有时不会
        driver_c_l.find_element_by_xpath(
            '//*[@id="HeaderContent"]/div/div/div/div[2]/div/div/div/div[4]/div[4]/div/a').click()
        time.sleep(3)
        driver_c_l.find_element_by_xpath(
            '//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/button/div').click()
        time.sleep(3)
        driver_c_l.find_element_by_xpath(
            '//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div').click()
        time.sleep(3)
        driver_c_l.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/input').send_keys(
            'E:\\video\\996.png')
        time.sleep(3)
        driver_c_l.execute_script("arguments[0].value = arguments[1]",
                                  driver_c_l.find_element_by_css_selector("textarea"), "打工人")
        # driver_c_l.find_element_by_id('pin-draft-title-ce467a4c-15ae-4400-9484-530684cbda0e').sent_keys('打工人')
        time.sleep(3)
        driver_c_l.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]').click()
        time.sleep(3)
    except:
        print("error")


def veoh_post():
    time.sleep(5)
    try:
        driver_c_l.find_element_by_xpath().send_keys()
        driver_c_l.find_element_by_xpath().click()
    except:
        print("error")


file = open("get_cookies.json")
t = json.load(file)

if t['name'] == 'twitter':
    twitter_post()
elif t['name'] == 'youtube':
    #暂时不能测试
    youtube_post()
elif t['name'] == 'facebook':
    facebook_post()
elif t['name'] == 'linkedin':
    linkedin_post()
elif t['name'] == 'vimeo':
    vimeo_post()
elif t['name'] == 'tiktok':
    tiktok_post()
elif t['name'] == 'pinterest':
    pinterest_post()
elif t['name'] == 'veoh':
    # 暂时不能测试
    veoh_post()
