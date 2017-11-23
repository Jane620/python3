#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import logging,threading,os
from datetime import datetime


class Log:
    def __init__(self):
        global logPath,resultPath,proDir
        # 获取上级目录
        proDir = os.path.abspath(os.path.join(os.getcwd(),'..'))
        print(proDir)
        resultPath = os.path.join(proDir,"result")
        # 判断是否存在文件夹
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 指定logpath的路径
        logPath = os.path.join(resultPath,str(datetime.now().strftime('%Y%m%d%H%M%S')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logPath,'output.log'))
        formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        handler.setFormatter(formater)
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log(self):

        if MyLog is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log
