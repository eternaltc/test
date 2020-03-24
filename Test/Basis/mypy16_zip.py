#测试zip()并行迭代
for i in [1,2,3]:
    print(i)

names = ("tc","one","tow","san")
ages = (23,35,67,45)
jobs = ("teacher","it","sir","polic")   #只有三个是则下面for只遍历三次

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

print()
for i in range(3):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))