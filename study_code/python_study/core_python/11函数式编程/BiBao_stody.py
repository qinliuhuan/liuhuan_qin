#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 17:06
# @Author  : QLH
# @Site    : 
# @File    : BiBao_stody.py
# @Software: PyCharm

def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


count = counter(5)
print(count())
print(count())
print(count())
count2 = counter(100)
print(count2())
print(count())
