# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 上午10:18
# @Author  : Jane
# @Site    : 
# @File    : MockDemo.py
# @Software: PyCharm


class Count:

    def add(self):
        pass

from unittest import mock
import unittest

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13)
        result = count.add(6)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()
