#-*- coding:utf-8 -*-

__author__ = 'wangjf'


"""
多种获取内省模块属性的方式
"""

import jenkins,sys


print(jenkins.BUILD_INFO)
print(jenkins.__dict__['BUILD_INFO'])
print(sys.modules['jenkins'].BUILD_INFO)
print(getattr(jenkins,'BUILD_INFO'))





