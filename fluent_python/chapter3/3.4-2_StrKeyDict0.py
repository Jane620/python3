#-*- coding:utf-8 -*-
'''在查询的时候把非字符串的键转换为字符串'''
'''
1. 当字典采用d[k]或d.get(k)的方法时候，默认调用dict的__getitem__方法
2. 假设找不到k，则先调用missing方法，之后因为missing方法重写了返回self[str(key)]，则继续调用__getitem__
3. 因此存在无限递归的情况，需要增加isinstance
'''

#继承与dict
class StrKeyDict0(dict):


    def __missing__(self, key):
        # 如果找不到的key本身就是str类型，则抛出异常
        if isinstance(key,str):
            raise KeyError(key)
        # 否则转换为字符串返回这个key
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # get方法以self[key]形式委托给_getitem__，因此查找失败后还能调用__missing__
            return self[key]
        except KeyError:
            # 如果__missing__也失败了，则返回None
            return default

    def __contains__(self, key):
        # 优先以自身的key进行查询value，不行则转换为字符串
        return key in self.keys() or str(key) in self.keys()



#test

if __name__ == "__main__":
    d= StrKeyDict0([('2','two'),('4','four')])
    print(d['2'])
    print(d[4])
    #print(d[1])
    print('get method ...')
    print(d.get('2'))
    print(d.get(4))