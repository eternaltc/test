#测试函数对象

def test01():
    print("双击666")

test01()
c = test01
c()

print(id(test01))   #打印id
print(id(c))
print(type(c))