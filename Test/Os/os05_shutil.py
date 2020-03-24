#coding=utf-8

import shutil
import zipfile
# shutil.copyfile("file03.txt","file05.txt")  #拷贝

# shutil.copytree("movie/大陆","电影")    #拷贝文件夹

#忽略不需要拷贝的文件
# shutil.copytree("movie/大陆","电影",ignore=shutil.ignore_patterns("*.txt","*.html"))

#压缩和解压缩
# shutil.make_archive("电影/压缩","zip","movie/大陆")


z1 = zipfile.ZipFile("a.zip","w")
z1.write("file05.txt")
z1.write("file03.txt")
z1.close()


#解压缩
z2 = zipfile.ZipFile("a.zip","r")
z2.extractall("电影")
z2.close()


