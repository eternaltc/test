#嵌套函数（内部函数）的定义

def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()

outer()

def printName(isChinese,name,familyName):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"小四","陶")
printName(False,"Ivanka","Trump")
printName(False,"tao","agle")

