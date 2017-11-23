#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import threading

def thread_fun(num):
    for n in range(int(num)):
        print('i came from {0}, num : {1}'.format(threading.current_thread().getName(),n))

def main(thread_num):
    thread_list = list()
    for i in range(thread_num):
        thread_name = 'thread_%s' %i
        thread_list.append(threading.Thread(target=thread_fun,name=thread_name,args=(20,)))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == '__main__':
    main(3)

