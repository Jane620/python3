#-*- coding:utf-8 -*-

__author__ = 'wangjf'

"""
mydir: a module list namespace of other modules
"""

seplen = 60
sepchr = '-'

def listing(module,verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:',module.__name__,'file',module.__file__)
        print(sepline)

    count = 0
    for attr in module.__dict__:
        print('%2d) %s' %(count,attr),end=' ')
        if attr.startswith('__'):
            print('<build-in name>')
        else:
            print(getattr(module,attr))
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__,'has %d namea' %count)
        print(sepline)

if __name__ == '__main__':
    import mydir
    listing(mydir)