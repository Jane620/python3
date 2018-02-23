#-*- coding:utf-8 -*-
import requests,json
__author__ = 'wangjf'


base_url = 'http://vempay-test.nfsq.com.cn/vem-admin/machineController/addMachineInfo'

datas = {
    'id' : 'NFHZ11000003',
    'ipcId':'NFHZ11000003',
    'machineModelId':'65',
    'machineType':'',
    'netId':'254',
    'office':'2934',
    'operatorId':'162',
    'pointId':'256',
    'status':'1'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://vempay-test.nfsq.com.cn/vem-admin-web/',
    'token' : 'b04b34eb83824e1d85105d90a65e6a19',
    'cookies':'SESSION=fafe7aab-5edb-4e48-8a1f-68388610df71; UM_distinctid=15df32e49ea595-0282bc158960e8-14396d54-13c680-15df32e49eb258'
}

rep = requests.post(base_url,data=datas,headers=headers)
print(rep.text)