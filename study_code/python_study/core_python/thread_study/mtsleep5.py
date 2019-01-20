# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 17:48
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : mtsleep5.py

import threading
from time import sleep, ctime
from myThread import MyThread

loops=[4,2]

# class MyThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)
#         self.name=name
#         self.func=func
#         self.args=args
#
#     def run(self):
#         # apply(self.func, self.args)
#         self.res = self.func(*self.args)

def loop(nloop, nsec):
    print('start loop ', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: ', ctime())

def main():
    print('starting at: ', ctime())
    threads=[]
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()


    print('all Done at: ', ctime())


if __name__ == '__main__':
    main()