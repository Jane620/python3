#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,re
from bs4 import BeautifulSoup

url = 'http://ci.yst.com.cn/view/持续集成/job/food-service/29/console'

rep = requests.get(url)
reg = re.compile(r'.*[\d]+/dashboard')

match = re.findall(reg,rep.text)


print(match)