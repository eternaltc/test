s = input("输入一个数字：")


# if int(s)<10:
#     print("{}是小于10的数字".format(s))
# else:
#     print("{}是大于等于10的数字".format(s))

print("{}是小于10的数字".format(s) if int(s)<10 else "{}是大于等于10的数字".format(s))