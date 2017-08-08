#-*- coding:utf-8 -*-


DIC = {'A':1, 'B':2, 'C':3}

def getitem(dict):
    item = None
    for key,value in dict.items():
        if key == 'C':
            item = value
        else:
            item = None
    return item

key = getitem(DIC)
print(key)