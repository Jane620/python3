#-*- coding:utf-8 -*-

'''
#仅做类型转换，且限制传入的为utf-8类型
'''


'''
#无论传入，均转换为str，即utf-8编码
'''
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


'''
#无论传入，均转换为bytes,即unicode编码
'''
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

