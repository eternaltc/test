#测试选择结构的嵌套
score = int(input("请输入一个0-100的数字："))
grade = ""

if score>100 or score<0:
    score = int(input("输入错误，请输入一个0-100的数字："))
else:
    if score >90:
        grade = "A"
    elif score >=80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "E"
    print("分数是{0}，等级是{1}".format(score,grade))

print("*******************************************")

score = int(input("请输入一个0-100的数字："))
grade = "ABCDE"
num = 0

if score>100 or score<0:
    score = int(input("输入错误，请输入一个0-100的数字："))
else:
    num = score//10
    if num<6:num=5
    if num==10:num=9
    grade = grade[9-num]
    print("分数是{0}，等级是{1}".format(score,grade))