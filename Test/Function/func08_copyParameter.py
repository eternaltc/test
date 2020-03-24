#传递不可变对象时，不可变对象里面包含子对象是可变的，则方法修改
#了这个可变对象，源对象也发生改变

a = (1,2,[3,4])
print("a:",id(a))

def test01(m):
    print("m:",id(m))
    m[2][0] = 20  #列表对象可变
    print(m)
    print("m:",id(m))

test01(a)
print(a)
