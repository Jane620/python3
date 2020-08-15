# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: test2.py
@time: 2019/8/29 15:44
@desc:
'''
import pytest

def test_raise():
    with pytest.raises(TypeError) as e:
        connect('localhost', '6735')
    exec_msg = e.value.args[0]
    assert exec_msg == 'port type must be int'

