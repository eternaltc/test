#测试while循环
num = 0
while num<=10:
    print(num,end="\t")
    num +=1

print()
print("**************************")

#计算1-100累加
num1 = 0
sum_all = 0
while num1<=100:
    sum_all = sum_all + num1
    num1 +=1
print("1-100累加为",sum_all)