#测试返回值的基本类型

def add(a,b):
    '''计算两个和'''
    print("{0}+{1}={2}".format(a,b,(a+b)))
    return a+b

def test02():
    print("six")
    print("6666")

    return   #1.返回值，2.结束函数执行
    print("hello")  #被结束

def test03(x,y,z):   #多个返回值
    return [x*10,y*10,z*10]

c = add(20,50)
print(add(20,30)*10)
print("*****************")

d = test02()
print(d)
print("*****************")

print(test03(2,3,4))