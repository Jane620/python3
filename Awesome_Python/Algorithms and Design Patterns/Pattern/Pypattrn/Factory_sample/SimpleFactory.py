# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: SimpleFactory.py
@time: 2019/1/4 14:41
@desc:
创建两个工厂用于处理不同的数据类型
'''
import json
import xml.etree.ElementTree as etree

class JsonConnector:

    def __init__(self,filepath):
        self.data = dict()
        with open(filepath,mode="r",encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


class XmlConnector:

    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parse_data(self):
        return self.tree

# 选择器,根据文件结尾来确定采用什么工厂
def connect_factory(filepath):

    if filepath.endswith("json"):
        connector = JsonConnector
    elif filepath.endswith("xml"):
        connector = XmlConnector
    else:
        raise ValueError("Cant connect to {0}".format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connect_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


if __name__ == '__main__':
    filepath = "test.json"
    filepath2 = "test.xml"

    #json_factory = connect_to(filepath)
    json_factory = JsonConnector(filepath)
    xml_factory = connect_to(filepath2)

    json_data = json_factory.parse_data
    xml_data = xml_factory.parse_data

    print(json_data)
    print(xml_data)

