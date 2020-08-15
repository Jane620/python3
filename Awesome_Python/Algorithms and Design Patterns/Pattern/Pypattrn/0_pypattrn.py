# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 0_pypattrn.py
@time: 2019/1/2 16:47
@desc:
'''

from pypattyrn.behavioral.chain import Chain,ChainLink


class ConcreateChainLinkTree(ChainLink):

    def handle(self, request):

        if request == "handle_three":
            return "Handle in chain link three"
        else:
            return self.successor_handle(request)


class ConcreateChainLinkTwo(ChainLink):

    def __init__(self):
        super().__init__()
        self.set_successor(ConcreateChainLinkTree()) # set to three instance

    def handle(self, request):

        if request == "handle_two":
            return "Handle in chain link two"
        else:
            return self.successor_handle(request)


class ConcreateChainLinkOne(ChainLink):

    def __init__(self):
        super().__init__()
        self.set_successor(ConcreateChainLinkTwo()) # set to three instance

    def handle(self, request):

        if request == "handle_one":
            return "Handle in chain link one"
        else:
            return self.successor_handle(request)

class ConcreteChain(Chain): # This object is a Chain

    def __init__(self): # Override init to initialize a Chain with the starting chain link.
        super().__init__(ConcreateChainLinkOne()) # Initialize this Chain with a start chain link.
                                                 # (a ConcreteChainLinkOne instance)

    def fail(self): # Implement the fail method, this is called if no chain links could handle a request.
        return 'Fail'


if __name__ == '__main__':

    chain = ConcreteChain()
    print(chain.handle("handle_one"))
    print(chain.handle("handle_four"))