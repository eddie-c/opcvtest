from selenium.webdriver.common.proxy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
phantomjs_path = r"d:/phantomjs.exe"
service_args = [
    '180.113.244.154:8123',
    '--proxy-type=http',
    ]

driver = webdriver.PhantomJS(executable_path=phantomjs_path,service_args=service_args)
# driver = webdriver.PhantomJS(service_args=service_args)
driver.get("http://httpbin.org/ip")
print driver.page_source.encode('utf-8')
# print "="*70
# print driver.title
# driver.save_screenshot(r"E:\Software & Tutorial\Phantom\test.png")
driver.quit()
