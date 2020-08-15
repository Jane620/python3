# -*- coding:utf-8 -*-
'''
@author: 
@software: Pycharm
@file: list_basic.py
@time: 2019/11/20 14:33
@desc: list basic functions
@source: https://www.runoob.com/python/python-lists.html
'''
import pytest
import operator


@pytest.fixture
def basic_list():
    return ["a", "b", "c", "d", "e"]


# this is not use any more in Py 3X
# instand of cmp , you can use operator.eq
def test_cmp(basic_list):
    list_cmp = ["a", "b", "c", "d", "e"]
    assert operator.eq(basic_list, list_cmp)


def test_len(basic_list):
    assert len(basic_list) == 5


def test_max(basic_list):
    assert max(basic_list) == "e"


def test_min(basic_list):
    assert min(basic_list) == 'a'


def test_list(basic_list):
    tuple_basic = ("a", "b", "c", "d", "e")
    assert list(tuple_basic) == basic_list
    str_basic = "hello"
    assert list(str_basic) == ["h", "e", "l", "l", "o"]


def test_append(basic_list):
    basic_list.append("f")
    assert basic_list == ["a", "b", "c", "d", "e", "f"]


def test_count(basic_list):
    basic_list.append("a")
    assert basic_list.count("a") == 2


def test_slice(basic_list):
    b2d = slice(1, 3)
    assert basic_list[b2d] == ["b", "c"]
