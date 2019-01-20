# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 11:38
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : mtsleep2.py

import _thread as thread
from time import sleep, ctime

loops = [3, 5]


def loop(nloop, nsec, lock):
    print("start loop ", nloop, ' at :', ctime())
    sleep(nsec)
    print('loop ', nloop, 'done at :', ctime())
    lock.release()


def main():
    print("starting at : ", ctime())
    locks = []
    nloops = range(len(loops))
    # print("nloops: ", nloops)

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    # print('locks: ', locks)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            print("The loop %s still locked" % (i))
            sleep(1)

    print("all Done at: ", ctime())


if __name__ == '__main__':
    main()
