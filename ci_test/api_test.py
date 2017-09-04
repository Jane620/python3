#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests

valid_url = 'api/authentication/validate'
index_url = 'api/projects/index'
dulicate_url = 'api/duplications/show'
coverage_url = 'api/coverage/show'
metrics = 'api/metrics'
resource = 'api/resources'
# GET 获取各项指标
domains = 'api/metrics/domains'

url = 'http://10.3.0.43:9000/' + resource

# 代码覆盖率 metrics = coverage
# 单元测试成功 metrics = test_success_density
# 重复 metrics = duplicated_lines_density
param = {
    'resource':'1',
    'metrics':'coverage'
}

r = requests.get(url,params=param)
res = r.json()

#print(res)

def printer():
    metrics = 'api/metrics'
    url = 'http://10.3.0.43:9000/' + metrics
    r = requests.get(url)
    res = r.json()

    data = {}
    for _,value in enumerate(res):
        key = value.get('key')
        name = value.get('name')
        data[key] = name
    return data


metric_resource = printer()
print(metric_resource)