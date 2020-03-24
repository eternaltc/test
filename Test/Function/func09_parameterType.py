#测试参数类型

def test(a,b,c,d):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

def test01(a,b,c=30,d=40):    #默认值参数传递,必须位于普通参数后面
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))

test(1,2,3,4)  #默认为位置参数
test(b =30,c=20,a=10,d=60)  #命名参数

test01(1,2)     #默认值参数
test01(1,2,3)

