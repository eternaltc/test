class Person:
    def __init__(self,name,age):
        self.name = name
        # self.age = age
        self.__age = age

    def say_age(self):
        print("年龄，我也不知道")

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)   #必须显式的调用父类初始化方法，不然解释器不会去调用
        self.score = score

#Student————>Person————>object类

print(Student.mro())
a = Student("tc",18,60)
a.say_age()

print(a.name)
print(dir(a))    #a的所有属性
print(a._Person__age)

