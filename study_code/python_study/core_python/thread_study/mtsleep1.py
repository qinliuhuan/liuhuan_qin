# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 11:31
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : mtsleep1.py

import _thread as thread
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
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all DONE at : ", ctime())


if __name__ == '__main__':
    main()