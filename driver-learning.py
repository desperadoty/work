from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import codecs

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.jianshu.com/u/c1e23027d245")

html = driver.page_source

bsobj = BeautifulSoup(html,'html.parser')
bsobj.encode('utf-8')

with codecs.open('index.html','w+',encoding='utf-8') as f:
    f.write(bsobj.prettify())

bsobj2 = BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
get_tag = bsobj2.link

print(get_tag)
print(get_tag.attrs)
print(get_tag['href'])
print(get_tag['media'])
print(get_tag['rel'])