#-*- coding:utf-8 -*-
import requests
from .readConfig  import ReadConfig
from .Log import MyLog

__author__ = 'wangjf'

localReadConfig = ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host,port,timeout
        host = localReadConfig.get_Http('baseurl')
        port = localReadConfig.get_Http('port')
        timeout = localReadConfig.get_Http('timeout')
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.header = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = host + url

    def set_header(self,header):
        self.header = header

    def set_params(self,params):
        self.params = params

    def set_files(self,file):
        self.files = file

    def get(self):
        try:
            respone = requests.get(self.url,params=self.params,headers=self.header,timeout=float(timeout))
            return respone
        except TimeoutError:
            self.logger.error('Time out!')
            return None

    def post(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.header, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('Time out!')
            return None





