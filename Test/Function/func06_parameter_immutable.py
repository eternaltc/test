#测试不可变对象参数的引用

a = 100

def test01(n):
    print("n:",id(n))  #传递进来的是a对象的地址
    n = n +20
    print("n:",id(n))   #创建新的对象n
    print(n)    #n变成新的对象

test01(a)
print("a:",id(a))