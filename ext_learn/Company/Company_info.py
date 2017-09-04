#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,re
from bs4 import BeautifulSoup

url = 'http://www.maigoo.com/news/467451.html'

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

fixed_html = soup.prettify()

#print(fixed_html)

td = soup.script.contents
print(soup.script)
print(td)