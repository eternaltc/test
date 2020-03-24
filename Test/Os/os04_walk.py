#coding=utf-8
#测试walk变量子目录和子文件
import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)

for dirpath,dirnames,filenames in list_files:
    for dir in dirnames:
        print(os.path.join(dirpath,dir))

    for file in filenames:
        # print(os.path.join(dirpath,file))
        all_files.append(os.path.join(dirpath,file))

print("####################")

#打印所有的子目录和子文件
for file in all_files:
    print(file)

    