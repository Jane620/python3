# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 3_garagy.py
@time: 2019/1/7 14:14
@desc:
'''


'''
Its a parking issue, need find the least movement to reach the goal
start = [1,2,3,0,4] , 0 is no car ,and 1234 are diffent car
end = [0,3,2,1,4]

So the step of move car is :
[0,2,3,1,4] ,change 1 to 0
[2,0,3,1,4] ,change 2 to 0
[2,3,0,1,4] ,change 3 to 0
[0,3,2,1,4] ,change 2 to o 
Need step 4
'''


def garage(initial, final):

    init = initial      # prevent changes in original 'initial'
    seq = []                   # list of each step in sequence
    steps = 0
    while init != final:
        # 获取当前init列表中0的位置
        zero = init.index(0)
        if zero != final.index(0):  #
            car_to_move = final[zero]   # 查看对应在final中的位置的值
            pos = init.index(car_to_move)         # 获取fina位置的值在init中的位置
            init[zero], init[pos] = init[pos], init[zero]  #将init中0所在位置与fina中对应位置的值两个值进行位置调换
        else:
            # 将从头开始往下获取到的不相等的值与init中0所在位置进行兑换
            for i in range(len(init)):
                if init[i] != final[i]:
                    init[zero], init[i] = init[i], init[zero]
                    break
        seq.append(init[::])
        #seq.append(init)
        steps += 1

    return steps, seq


'''
思路：从尾到头进行数字调换，且只能与0进行调换  //错误，因为每次获取的固定是final的0的位置，替换位置的时候可能并非是0进行交换的
1. 先找到0的在开始列表的位置，对比结果列表，不相同则进行替换，相同则进行前一位的对比
'''
def fake_garage(initial,final):

    init = initial # make a copy to prevent init change , not nesserary?
    steps = 0
    seq = []

    # 优先判断两则不相同，则循环
    while init != final:
        # 首先获取0所在的位置，即空停车位的地址
        zero = final.index(0)
        if zero != initial.index(0): # 如果两则的0位置不同，则xx
            car_to_move = init[zero]  # 找对应final 中 0 对应final所在位置应该挪动的车
            pos = final.index(car_to_move) # 找到init中对应final应该移动车的位置
            init[zero] , init[pos] = init[pos] , init[zero]
        else:
            for i in range(len(init)):
                if init[i] != final[i]:
                    init[zero], init[i] = init[i], init[zero]
                    break
        # 只能append当前list的copy，因为list是可变的，因此不能直接用本体
        seq.append(initial[::])
        # 每交换一次则记录一次次数
        steps += 1
    return steps , seq



if __name__ == '__main__':
    start = [1,3,2,4,6,0]
    end = [3,6,4,1,2,0]

    #steps , seq = fake_garage(start,end)
    steps, seq = garage(start, end)

    print("step:{0},seq:{1}".format(steps , seq))
