# -*- coding:utf-8 -*-

import time
from selenium import webdriver
import requests
from fake_useragent import UserAgent
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



SERVICE_ARGS = ['--load-images=false', '--disk-cache=true','--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']



PROXY = '180.113.244.154:8123'
# print PROXY

# proxy = Proxy(
#     {
#         'proxyType': ProxyType.MANUAL,
#         'httpProxy': PROXY  # 代理ip和端口
#     }
# )


options = webdriver.ChromeOptions()
options.add_argument('--proxy-server='+PROXY)
driver = webdriver.Chrome(chrome_options=options)
# driver.get("http://httpbin.org/ip")
driver.get('http://httpbin.org/ip')
print(driver.page_source)