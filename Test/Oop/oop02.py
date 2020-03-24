class Student:
    # pass
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是:{1}".format(self.name, self.score))

print(type(Student))
print(id(Student))

s1 = Student("陶垂", 20)
s1.say_score()

Stu2 = Student
s2 = Stu2("小三",70)
s2.say_score()

