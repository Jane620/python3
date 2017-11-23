# -*- coding:utf-8 -*-

__author__ = 'wangjf'

import os, codecs, configparser

'''
读取对应的config.ini中配置信息
'''

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, 'Config.ini')

class ReadConfig:
    '''
    传入config的path
    '''

    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        # 去掉BOM_UTF8
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, 'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get('DATABASE', name)
        return value

    def get_Http(self, name):
        value = self.cf.get('HTTP', name)
        return value