try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
    # print(c)
except BaseException as e:
    print(e)
else:
    print(c)
