from time import sleep

from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://baidu.com")

sleep(5)

wd.close();