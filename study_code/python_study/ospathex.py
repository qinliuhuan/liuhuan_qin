# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 22:36
# @Author  : 11382 
# @Email   : 1138266752@qq.com
# @File    : ospathex.py

import os
current_path = os.getcwd()
print("Current path is: %s" % current_path)
tmp_file = current_path + '\tmp.txt'
for  tmpdir in ('/tmp', r'c: \temp'):
    if os.path.exists(tmpdir):
        break

else:
    print("No temp direatory avaliable")
    tmpdir = current_path

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print("*** current temporary directory")
    print("cwd is : ", cwd)

    print("*** creating example directory...")
    if not os.path.exists(current_path+ '\example'):
        os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print("now the current path is :%s" % cwd)
    print("*** original directory listing is %s" % os.listdir(cwd))
    print("*** createing test file...")
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print("*** updated directory listing")
    print(os.listdir(cwd))

    print("*** ranaming 'test' to 'filetest.txt")
    if not os.path.exists(cwd + '/filetest.txt'):
        os.rename('test', 'filetest.txt')
    print("*** updated directory listing:")
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print("*** full file pathname: ", path)
    print("*** (patchname, basename) == " ,os.path.split(path))
    print("*** (filename, extension) ==  " ,os.path.splitext(os.path.basename(path)))

    print(" display file contents: ")
    fobj = open(path)
    for eachLine in fobj:
        print("eachLine = ", eachLine)
    fobj.close()

    print("deleting test file")
    if os.path.exists(path):
        os.remove(path)
    print(" update directory listing： ")
    print(os.listdir(cwd))
    os.chdir(os.pardir)
    print("deleting test directory")
    os.rmdir('example')
    print("Done")

