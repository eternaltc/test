import time

start = time.time()
for i in range(1000):
    result = []  # #列表清空
    for m in range(10000):
        result.append(i*1000+m*100)

end = time.time()
print(result)     #打印最后循环的列表
print("耗时：{0}".format(end-start))


start1 = time.time()
for i in range(1000):
    result = []    #列表清空
    c = i*1000
    for m in range(10000):
        result.append(c + m * 100)

end1 = time.time()
print(result)
print("耗时：{0}".format(end1 - start1))


