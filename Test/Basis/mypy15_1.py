import time

start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)

end = time.time()
print("耗时：{0}".format(end-start))


start1 = time.time()
for i in range(10):
    result = []    #列表清空
    c = i*10
    for m in range(10):
        result.append(c + m * 10)
        print(result)     #打印最后循环的列表
end1 = time.time()
print(result)
print("耗时：{0}".format(end1 - start1))
print("************************************************")

start2 = time.time()
result = []         #列表全部累加到一起
for i in range(10):
    c = i*10
    for m in range(10):
        result.append(c + m * 10)
        print(result)   #打印出所有循环的列表
end1 = time.time()
print(result)
print("耗时：{0}".format(end1 - start1))