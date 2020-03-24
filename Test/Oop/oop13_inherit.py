class Person:
    def __init__(self,name,age):
        self.name = name
        # self.age = age
        self.__age = age

    def say_age(self):
        print("年龄:",self.__age)

    def say_introduce(self):
        print("我的名字：",self.name)

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)   #必须显式的调用父类初始化方法，不然解释器不会去调用
        self.score = score

    def say_introduce(self):
        """重写父类的方法"""
        print("大家好，我的名字是:{0}".format(self.name))

s = Student("陶垂",18,60)  #调用子类
s.say_introduce()
s.say_age()

s2 = Person("一万",6)   #调用父类
s2.say_introduce()
