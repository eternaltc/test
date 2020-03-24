class Student:  #类名一般首字母大写，多个单词采用驼峰原则,eg:GoodStudent
    #定义属性，构造方法
    def __init__(self,name,score): #self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是:{1}".format(self.name,self.score))

s1 = Student("陶垂",20)
s1.say_score()

s1.age = 18
s1.salary = 3000
# del s1
print(s1.salary)

s2 = Student("三四",60)
s2.say_score()

print(dir(s2))
print(s2.__dict__)
print(isinstance(s2,Student))   #判断s2是否是Student类


