import os

path = os.getcwd()

old_file = path + '/1.conf'
data = ''
ff = open(old_file, 'r')
if 'max' in ff.read():
    print('max 在这里面')
    ff.close()
    with open(old_file, 'r+') as f:
        for line in f.readlines():
            if (line.find('max') == 0):
                line = 'max=600' + '\n'
            data += line

    with open(old_file, 'r+') as f:
        f.writelines(data)
else:
    print('max 不在这里面')
    ff.close()
    with open(old_file, 'a+') as f:
        tmp = '\n' + 'max=1200' + '\n'
        f.write(tmp)
        f.close()





    # if 'f' not in f.read():
    #     print('not in')
    #     f.write('f=45555')
    # else:
    #     print('in')
    #     f.writelines(data)


