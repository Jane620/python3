#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests
from bs4 import BeautifulSoup

url = 'https://www.phb123.com/qiye/9005.html'

req = requests.get(url).content

soup = BeautifulSoup(req.decode('utf8'),'html.parser')

print(soup)