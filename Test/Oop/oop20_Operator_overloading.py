#测试运算符重载
class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不同同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不同同类对象，不能相乘"

p1 = Person("对三")
p2 = Person("炸你")

x = p1 + p2
print(x)

print(x*30)
