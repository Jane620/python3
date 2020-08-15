# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: test3.py
@time: 2019/8/29 15:48
@desc:
'''
import pytest

@pytest.fixture()
def postcode():
    a = 1
    return '100'


def test_postcode(postcode):
    assert postcode.a == 1


