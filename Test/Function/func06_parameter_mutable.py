#测试可变对象的参数传递

a = [10,20]
print(id(a))
print("*************")

def test01(m):
    print(id(m))
    m.append(30)
    print(id(m))

test01(a)
print(a)
