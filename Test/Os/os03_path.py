#coding=utf-8

import os
from os import path

# import os.path
# print(os.path.isabs("d:/a.txt"))   #判断是否为绝度路径

#判断
print(path.isabs("D:/a.txt"))    #判断是否为绝度路径True
print(path.isdir("d:/a.txt"))   #判断是否为目录False
print(path.isfile("d:/a.txt"))  #判断是否为文件True
print(path.exists("d:/a.txt"))  #判断文件是否存在

#获取文件基本信息
print(path.getsize("file03.txt"))  #文件大小
print(path.abspath("file03.txt"))  #绝对路径
print(path.dirname("d:/file03.txt"))  #所在目录

print(path.getctime("file03.txt"))   #创建时间
print(path.getatime("file03.txt"))   #最后访问时间
print(path.getmtime("file03.txt"))   #最后修改时间

#对路径操作
path = path.abspath("file03.txt")
print(path)
print(os.path.split(path))
print(os.path.splitext(path))

print(os.path.join("aa","bb","cc"))


