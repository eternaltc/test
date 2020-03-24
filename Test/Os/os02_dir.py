#coding=utf-8
#测试os模块。操作文件和目录
import os


print(os.name)    #判断系统windows->nt   linux和unix->posix
print(os.sep)     #分隔符windows->\   linux和unix->/
print(repr(os.linesep))   #换行符windows->\r\n   linux和unix->\n
print(os.stat("os02_dir.py"))   #文件信息

#文件工作目录
print(os.getcwd())
# os.chdir("d:")   #改变工作目录为D盘

#创建目录、多级目录、删除
# os.mkdir("书籍")    #相对于当前工作目录,创建目录
# os.rmdir("书籍")    #删除目录

# os.makedirs("电影/大陆/周星驰")     #创建多级目录
# os.removedirs("电影/大陆/周星驰")   #只能删除空目录

# os.makedirs("../音乐/四川/鞠婧祎")   #../上级目录

# os.rename("电影","movie")       #更改目录名字
dirs = os.listdir("movie")      #返回该目录下的文件
print(dirs)



