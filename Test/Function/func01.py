#测试函数定义和使用
#函数名符合标识符规则

def test01():
    print("*"*10)
    print("#"*10)

print(id(test01))
print(type(test01))
print(test01)

test01()
test01()

for i in range(5):
    test01()