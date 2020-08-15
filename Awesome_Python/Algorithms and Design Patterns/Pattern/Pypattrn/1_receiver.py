# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 1_receiver.py
@time: 2019/1/2 17:08
@desc:
'''

from pypattyrn.behavioral.command import Command,Invoker,Receiver


class MyCommand(Command):

    def __init__(self,receiver,command,**kwargs):
        self.__command = command
        super().__init__(receiver)

    def execute(self):
        super().execute(self.__command)
        pass

    def unexecute(self):
        pass



class Thermostat(Receiver): # receiver object

    def raise_temp(self,amount):
        return "Tempurature raised by {0} degree".format(amount)

    def low_temp(self,amount):
        return "Tempurature lowed by {0} degree".format(amount)


class ExecutorCommand(MyCommand):

    def __init__(self,receiver,command,amount=5):
        super().__init__(receiver,command)
        self.amount = amount

    def execute(self):
        if self.command == "raise":
            return self._receiver.action("raise_temp",self.amount)
        elif self.command == "low":
            return self._receiver.action("low_temp", self.amount)
        else:
            return "do nothing"

    def unexecute(self):
        pass

class Worker(Invoker):

    def __init__(self):
        super().__init__(ExecutorCommand)


if __name__ == '__main__':

    thermostat = Thermostat()
    worker = Worker()

    assert "Tempurature raised by 5 degree" == worker.execute(ExecutorCommand(thermostat,"raise"))

