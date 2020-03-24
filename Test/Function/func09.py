#测试可变参数处理（元组、字典两种方式）

def test01(a,b,*c):   #一个星号
    print(a,b,c)

def test02(a,b,**c):  #两个星号,收集到元组
    print(a,b,c)

def test03(a,b,*c,**d):  #一个星号和两个星号
    print(a,b,c,d)

def test04(*a,b,c):     #强制命名参数
    print(a,b,c)

test01(1,2,3,4)
test02(1,2,name='tc',age=18)
test03(1,2,3,4,name='tc',age=18)
test04(1,2,b=3,c=4) #可变参数星号后面的必须强制命名
#test04(1,2,3)  #报错，a为可变参数，收集全部参数，b,c造成没有赋值


