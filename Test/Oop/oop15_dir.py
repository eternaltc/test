class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name ,"年龄：",self.age)

object = object()
print(dir(object))

s = Student("tc",18)
print(dir(s))

