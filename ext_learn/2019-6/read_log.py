# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: read_log.py
@time: 2019/6/6 16:28
@desc:
'''


filename = "fsp.log"


with open(filename,'r') as f:
    lines = f.readlines()
    for line in lines:
        pass
