#测试全局变量、局部变量

a = 3   #全局变量

def test01():
    b = 4   #局部变量
    print(b*10)

    global a    #如果要在函数内改变全局变量的值，增加global关键字声明
    a = 300
    print(a)

    print(locals())  # 打印输出局部变量
    print(globals())  # 打印输出全局变量

test01()

print(a)
#print(b)   #局部变量，报错NameError: name 'b' is not defined
print(locals())     #打印输出局部变量
print(globals())    #打印输出全局变量

