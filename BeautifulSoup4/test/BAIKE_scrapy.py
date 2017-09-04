
import requests,re
from bs4 import BeautifulSoup

__author__ = 'wangjf'

url = 'https://www.baidu.com/s?wd='

name = '深圳市海普瑞药业股份有限公司员工人数'

url = url + name

rep = requests.get(url)

soup = BeautifulSoup(rep.content.decode('utf-8'),'html.parser')

body= soup.find('body')

str = ''

print(body)

num = re.findall(re.compile(r'[\d]+.?[\d]+人'),str)
#print(''.join(num[0] if num else '0'))

