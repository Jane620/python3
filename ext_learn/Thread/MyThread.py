#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('I am %s' %self.name)


if __name__ == '__main__':
    for thread in range(5):
        t = MyThread()
        t.start()
