import codecs

from bs4 import BeautifulSoup
from selenium import webdriver

base_url = 'https://www.jianshu.com'
user = '/u/c1e23027d245'
phantomjs_path = '/Users/yvetteyoung/phantomjs-2.1.1-macosx/bin/phantomjs'

driver = webdriver.PhantomJS(executable_path=phantomjs_path)

driver.get(base_url+user)
html = driver.page_source

bsobj = BeautifulSoup(html)
bsobj.encode('utf-8')

with codecs.open('index.html','w+',encoding='utf-8') as f:
    f.write(bsobj.prettify())