# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 11:18
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : onetheread.py

from time import sleep, ctime

def loop0():
    print("start loop 0 at : ",  ctime())
    sleep(4)
    print("loop 0 done at : ", ctime())

def loop1():
    print("start loop 1 at : ", ctime())
    sleep(2)
    print("loop 1 done at : ", ctime())

def main():
    print("starting at : ", ctime())
    loop0()
    loop1()
    print("all DONE at : ", ctime())


if __name__ == '__main__':
    main()