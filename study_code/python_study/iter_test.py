# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 11:28
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : iter_test.py

myTuple = (123, 'xzc', 56.78)

# fetch = iter(myTuple)
#
# for i in fetch:
#     print(i)

# while True:
#     try:
#         i= fetch.__next__()
#         print(i)
#     except StopIteration:
#         break

tmp = [(x+1, y+1) for x in range(3) for y in range(5)]
print(tmp)