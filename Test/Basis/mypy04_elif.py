score = int(input("请输入分数："))
grade = ""

if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
else:
    grade = "优秀"

print("分数是{0}，等级是{1}".format(score,grade))
# print("分数是{}，等级是{}".format(score,grade))，建议写全