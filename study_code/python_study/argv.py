# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 22:00
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : argv.py

import sys

print("you entered: ", len(sys.argv), "arguments...")

print("they were: ", str(sys.argv))

print("The file name is ", sys.argv[0])
print("teh second argv is ", sys.argv[1])