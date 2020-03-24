#测试循环中的else语句
staffNum = 4
salaryNum = 0
salarys = []

for i in range(staffNum):
    s = input("请输入员工的薪资（Q或q退出）：")

    if s=="Q" or s=="q":
        break

    if float(s)<0:
        continue

    salarys.append(float(s))
    salaryNum += float(s)

else:
    print("已录入4个员工的薪资")

print("录入薪资{0}".format(salarys))
print("平均薪资{0}".format(salaryNum/staffNum))