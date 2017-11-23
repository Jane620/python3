#-*- coding:utf-8 -*-
from flask import Flask,request
import unittest
__author__ = 'wangjf'

class FlaskTestCase(unittest.TestCase):

    def test_aseer(self):
        self.app = Flask(__name__)
        with self.app.test_request_context('/?name=peter'):
            assert request.path == '/'
            assert request.args['name'] == 'peter'

if __name__ == '__main__':
    unittest.main()