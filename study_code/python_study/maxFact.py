# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 11:09
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : maxFact.py

def showMaxFactor(num):
    count = int(num / 2)
    while count > 1:
        # print("count %s" % count)
        if num % count == 0:
            print("largest factor of %d is %d" % (num, count))
            break
        count = count - 1

    else:
        print(num , "is prime")


for eachNum in range(10, 21):
    showMaxFactor(eachNum)