#-*- coding:utf-8 -*-
import cx_Oracle
__author__ = 'wangjf'


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def md5str(str1):
    str2 = list(str1)
    str_tmp = []
    np = len(str2)
    for i in range(len(str2)):
        str_tmp.append(chr(ord(str2[i]) ^ 3))
    return md5(''.join(str_tmp))

def write_file(psw_list):
    import csv
    with open('psw.csv','w') as f:
        writer = csv.writer(f)
        for i in psw_list:
            writer.writerow(i)


def batch_create():
    ts = '1496806432482'
    psw_list = []
    ip_list= ['10.213.3.199','10.213.3.45']
    for i in range(1,100001):
        vmId = 'NFHZ'
        uuid = '0a6131b0f7250e4a30e'
        begin = 9000000
        vmId = vmId + str(begin+i)
        uuid = uuid + str(begin+i)
        ipcid = vmId
        input = ts+vmId+uuid+'x`x``
        psw = md5str(input)
        import random
        ip = random.choice(ip_list)
        psw_list.append([ip,ipcid,vmId,uuid,psw])
    write_file(psw_list)

def single_create():
    ts = '1496806432482'
    psw_list = []
    vmId = 'TEMP00001'
    uuid = '0a6131b0f7250e4a30e'
    ipcid = 'TEMP00001'
    input = ts+vmId+uuid+'zfj&^*$!nfsq***yst'
    psw = md5str(input)
    psw_list.append([ipcid, vmId, uuid, psw])
    psw_list.append(['TEMP00002', 'TEMP00002', '0a6131b0f7250e4a30e', '142fa39dc7646f43b84efbf9460196fb'])
    write_file(psw_list)

if __name__ == '__main__':
    batch_create()
    #single_create()