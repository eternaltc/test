#测试局部变量、全局变量效率

import math
import time

def globalTset():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)   #及时30的平方根
    end = time.time()
    print("全局变量耗时{}".format(end-start))

def localTest():
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("局部变量耗时{}".format(end-start))

globalTset()
localTest()