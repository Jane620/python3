#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import re


str = '''
[food-service] $ /bin/sh -xe /tmp/jenkins3421967044110561948.sh
+ url=http://10.3.0.43:9000
+ project_name=food-service
+ python3 /home/jenkins/.python/sonar.py http://10.3.0.43:9000 food-service
代码覆盖率:1.5%,单元测试成功率:1.3%,代码重复率:0.0%
'''

reg = re.compile(r':[0-9]{1,3}.[0-9]%')

match = re.findall(reg,str)
print(match)