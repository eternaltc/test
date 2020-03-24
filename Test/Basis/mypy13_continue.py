#测试continue
staffNum = 0
salaryNum = 0
salarys = []

while True:
    s = input("请输入员工的薪资（Q或q退出）：")

    if s=="Q" or s=="q":
        break

    if float(s)<0:
        continue

    staffNum +=1
    salarys.append(float(s))
    salaryNum += float(s)
print("员工数{0}".format(staffNum))
print("录入薪资{0}".format(salarys))
print("平均薪资{0}".format(salaryNum/staffNum))
