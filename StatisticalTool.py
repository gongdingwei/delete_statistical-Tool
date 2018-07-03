#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0.01
@author: qingyao.wang
@license: kuang-chi Licence 
@contact: qingyao.wang@kuang-chi.com
@site: 
@software: PyCharm
@file: StatisticalTool.py
@time: 2018/7/2 16:10
"""

import os
import xml.etree.ElementTree as ET

rootdir = unicode('/home/asus/VOCdevkit/0712Img/test','utf-8')
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
index=0


xml=[]
mylist=[]
for tmp in list:    # 循环读取路径下的文件并筛选输出
    if os.path.splitext(tmp)[1] == ".xml":   # 筛选xml文件
        path = os.path.join(rootdir,tmp)
        tree = ET.parse(path)
        root = tree.getroot()

        for node in root.iter('name'):
            #print(node.tag,node.text)
            mylist.append(node.text)

myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复 项

fw=open('/home/asus/VOCdevkit/0712Img/test/data.txt','w')

for item in myset:
  print("the %s has found %s" %(item,mylist.count(item)))
  fw.write(("the %s has found %s\n" %(item,mylist.count(item))))

fw.close()


