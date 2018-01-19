# !/usr/bin/python
# -*- coding:utf-8 -*-

import  sys
reload(sys)
sys.setdefaultencoding('UTF8')

from functools import wraps
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
def main():
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser = webdriver.Chrome('/usr/local/bin/chromedriver')

        browser.set_page_load_timeout(30)
        browser.maximize_window()

        # try:
        print '开始登陆'
        browser.get('https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/portal/home.htm')
        filepath = r"cookies"
        file = open(filepath, "rb")
        cookiesarray = []
        print("start")
        for line in file:
            linstr = line.decode("utf-8", "ignore")  #
            itemlist = linstr.split("\t")
            cookiesarray.append(itemlist)
        print("end")
        file.close()

        cookiesdict = {}
        cookieResultsarray = []
        for item in cookiesarray:
            dict = {}
            dict['name'] = item[0]
            dict['value'] = item[1]
            dict['domain'] = item[2]
            if dict['domain'].startswith('.'):
                dict['domain'] = item[2]
            else:
                dict['domain'] = '.' + item[2]
            dict['path'] = item[3]
            dict['expires'] = item[4]
            if len(item) == 7 and len(item) != 8:
                dict['httpOnly'] = True
            else:
                dict['httpOnly'] = False

            if len(item) == 8:
                dict['secure'] = True
            else:
                dict['secure'] = False

            # cookieResultsarray.append(dict)
            if dict['domain'] in ['.taobao.com', '.sycm.taobao.com']:
                cookieResultsarray.append(dict)

        for cookie in cookieResultsarray:
            print cookie
            browser.add_cookie(cookie)

        print '添加cookies成功'

        browser.get('https://sycm.taobao.com/mq/industry/rank/industry.htm')

        wait = WebDriverWait(browser, 10)

        usernameInput = wait.until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="ebase-frame-header-userLink"]'))
        )

        if usernameInput:
            print '登陆成功'
main()