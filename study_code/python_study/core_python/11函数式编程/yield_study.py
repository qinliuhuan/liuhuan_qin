#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 22:40
# @Author  : QLH
# @Site    : 
# @File    : yield_study.py
# @Software: PyCharm


# def simpleGen():
#     yield 1
#     yield '2 --> punch!'
#
#
# myG = simpleGen()
# # print(myG.__next__())
# # print(myG.__next__())
# # print(myG.__next__())
#
# for eachItem in simpleGen():
#     print(eachItem)

# from random import randint
#
#
# def randGen(aList):
#     while len(aList) > 0:
#         yield aList.pop(randint(0, len(aList)))
#
#
# for item in randGen(['rock', 'paper', 'scissors']):
#     print(item)

import time


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


for eachItem in counter(5):
    time.sleep(0.5)
    print(eachItem)
    # if eachItem == 10:
    #     eachItem.close()
# count = counter(5)
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
