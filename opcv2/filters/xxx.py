# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver
import requests
from fake_useragent import UserAgent


def get_proxy():
    r = requests.get('http://localhost:5001/get')
    proxy = r.text
    return proxy



PROXY = 'http://27.46.74.41:9999'
# print PROXY
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/portal/home.htm')
# print(driver.page_source)
# time.sleep(15)
# driver.quit()



url = "https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/portal/home.htm"
ua = UserAgent()
base_headers = {
    'User-Agent': ua.random,
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
headers = base_headers
real_proxy = PROXY
proxies = {"http": real_proxy, }
r = requests.get(url, headers=headers, proxies=proxies,timeout=10)
print('Getting result', url, r.status_code)
if r.status_code == 200:
    print('Valid proxy', PROXY)
