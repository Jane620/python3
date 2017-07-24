import time

class myTime():

    def __init__(self):
        self.promp = '未开始计时'
        self.unit = ['年','月','日','时','分','秒']
        self.lasted = []
        self.begin = 0
        self.end = 0

    def start(self):
        self.begin = time.localtime()
        print('计时开始')

    def stop(self):
        self.end = time.localtime()
        self._cTime()
        print('计时结束')

    #内部方法，采用_方式
    def _cTime(self):
        self.lasted = []
        self.promp = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index] == 0:
                continue
            self.promp += str(self.lasted[index]) + str(self.unit[index])
        print(self.promp)

t1 = myTime()
t1.start()
time.sleep(2)
t1.stop()