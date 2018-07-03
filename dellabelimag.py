#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0.01
@author: qingyao.wang
@license: kuang-chi Licence 
@contact: qingyao.wang@kuang-chi.com
@site: 
@software: PyCharm
@file: test.py
@time: 2018/6/26 17:42
"""


import os,shutil



def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print "copy %s -> %s"%( srcfile,dstfile)





rootdir = unicode('/home/asus/project/darknet/test_c2','utf-8')
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
index=0


xml=[]
jpg=[]

for tmp in list:    # 循环读取路径下的文件并筛选输出
    if os.path.splitext(tmp)[1] == ".xml":   # 筛选csv文件
        xml.append(tmp)
        #print tmp
    if os.path.splitext(tmp)[1] == ".jpg":   # 筛选csv文件
        jpg.append(tmp)


for i in jpg:
    (shotname,extension) = os.path.splitext(i)
    #print  shotname,extension
    if shotname+".xml"  not in xml:
        path = os.path.join(rootdir,i)
        os.remove(path)


