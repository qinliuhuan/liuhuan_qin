# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 18:01
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : myThread.py

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def getResult(self):
        return self.res

    def run(self):
        print('starting ', self.name, 'at: ', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at: ', ctime())