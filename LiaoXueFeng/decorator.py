#-*- coding:utf-8 -*-

__author__ = 'wangjf'

def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('{0} call {1} '.format(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('test text')
def now():
    print('2017-11-3')



if __name__ == '__main__':
    f = now()
    #print(now.__name__)