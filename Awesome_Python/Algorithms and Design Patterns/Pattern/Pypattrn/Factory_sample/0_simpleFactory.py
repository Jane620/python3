# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 0_simpleFactory.py
@time: 2019/1/8 15:08
@desc:
'''

import json
import xml.etree.ElementTree as etree


class DataFactory:

    def __init__(self,filepath):
        self.filepath = filepath

    class JsonFactory:
        def __init__(self,filepath):
            self.data = dict()
            with open(filepath,mode="r",encoding="utf-8") as f:
                self.data = json.loads(f)

    class XmlFactory:

        def __init__(self,filepath):
            self.data = etree.parse(filepath)


    def parseData(self):

        if self.filepath.endswith(".json"):
            return self.JsonFactory(self.filepath)
        elif self.filepath.endswith(".xml"):
            return self.XmlFactory(self.filepath)
        else:
            return "I dont recognized this file."