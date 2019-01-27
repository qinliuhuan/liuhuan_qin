#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 15:06
# @Author  : QLH
# @Site    : 
# @File    : pfa_study.py
# @Software: PyCharm

from functools import partial
# import _tkinter as Tkinter
import tkinter as Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='Quit', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('FPAS!')
root.mainloop()
