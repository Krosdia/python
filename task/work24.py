import random
import string
import os
from os.path import splitext

def gen_code(len=4):
    #随机生成4位验证码
    li = random.sample(string.ascii_letters+string.digits,len)
    #拼接为字符串
    return ''.join(li)

def create_files():
    #随机生成100个验证码
    li = [gen_code() for i in range(100)]
    os.mkdir('img')
    for i in li:
        os.mknod('img/' + i + '.png')

create_files()

def modify_suffix(dirname,old_suffix,new_suffix):
    #找出以png结尾的文件名
    # pngfile = [filename for filename in os.listdir(dirname) if filename.endswith(old_suffix)]
    pngfile = filter(lambda filename:filename.endswith(old_suffix),os.listdir(dirname))

    #分离文件名和后缀
    basefiles = [os.path.splitext(filename)[0] for filename in pngfile]

    #文件重命名
    for filename in basefiles:
        # print(filename)
        oldname = os.path.join(dirname,filename + old_suffix)
        newname = os.path.join(dirname,filename + new_suffix)
        os.rename(oldname,newname)
        print('%s重命名为%s成功' %(oldname,newname))

modify_suffix('img','.png','.jpg')
