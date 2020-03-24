#打印出报错的详细信息

import traceback
try:
    num = 1/0
except:
    traceback.print_exc()

#将异常信息输出到指定文件
import traceback
try:
    num = 1/0
except:
    with open("E:\学习\python学习\学习笔记\学习文档\测试.txt", "a") as f:
        traceback.print_exc(file=f)


