#https://m.stock.naver.com/index.html#/domestic/stock/005930/news
#https://m.stock.naver.com/index.html#/worldstock/stock/TSLA.O/news
#https://m.stock.naver.com/index.html#/worldstock/stock/TSM/news
#https://m.stock.naver.com/index.html#/worldstock/stock/LCID.O/news
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver=webdriver.Chrome()

domestic_or_world='worldstock'
code_or_name='TSLA.O'
url='https://m.stock.naver.com/index.html#/'+domestic_or_world+'/stock/'+code_or_name+'/news'
driver.get(url)
html=driver.page_source
soup = BeautifulSoup(html)
titles=soup.select('body>div#root>div#content>div')[5].select('ul>li')
list_title=[]
for i in titles:
    a=i.select('div>a>div>img')[0]['alt']
    print(a)
    list_title.append(a)
