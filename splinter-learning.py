# from splinter.browser import Browser
#
# with Browser("chrome") as browser:
#     url = "http://www.baidu.com"
#     browser.visit(url)
#     browser.fill("wd","ready player one")
#     button = browser.find_by_id('su')
#     button.click()


# -*- coding: utf-8 -*-
# from splinter.browser import Browser
#
# b = Browser("chrome")
# b.visit("http://www.baidu.com")
# dict={"wd":"splinter"}
# #b.fill("wd","splinter")
# b.fill_form(dict)
# button = b.find_by_id('su')
# button.click()

from splinter.browser import Browser
browser = Browser("chrome")
url = "http://www.baidu.com"
browser.visit(url)
browser.fill('wd','ready player one')
button = browser.find_by_id('su')
button.click()