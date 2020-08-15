# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: test_sumary.py
@time: 2019/10/8 15:34
@desc:
'''

import pytest

@pytest.fixture
def error_fixture():
    assert 0

def test_ok():
    print("test pass")

def test_fail():
    x = 1
    assert 0

def test_error(error_fixture):
    pass

def test_skip():
    pytest.skip("skipping this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always failed")
def test_xpass():
    pass