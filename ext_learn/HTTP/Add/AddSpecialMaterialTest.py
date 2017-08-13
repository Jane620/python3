#-*- coding:utf-8 -*-
import requests

'''
传入带路径的文件名，输出拼接好的字典
'''
def readfile(filename):
    data = {}
    with open(filename, 'r') as fileProcess:
        for line in fileProcess.readlines():
            key = line.strip('\n').split('=')[0]
            value = line.strip('\n').split('=')[1]
            data[key] = value
    return data

def sendHttpRequest(filename):

    url = readfile(filename)['loginurl']
    data = readfile(filename).copy()
    data.pop('loginurl')
    # data还是json可以直接通过chrome中F12接口方式
    response = requests.post(url, data=data)
    print('返回码：{0}，返回信息：{1}'.format(response.status_code, response.text))
    #writeConfig(r.text)

def writeConfig():
    # 将输出结果写入配置文件，以key=value方式
    pass

fileName = r'..\resource\config'
sendHttpRequest(fileName)