#-*- coding:utf-8 -*-
import requests
__author__ = 'wangjf'


url = 'http://ci.yst.com.cn/view/持续集成/job/vem-operator-sonar/lastBuild/jacoco/api/python?pretty=true'
re = requests.get(url)
print(re.json())