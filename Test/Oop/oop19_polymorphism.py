class Man:
    def eat(self):
        print("吃饭方式：")

class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):
    def eat(self):
        print("英国人用刀叉吃饭")

class Indian(Man):
    def eat(self):
          print("印度人用手吃饭")

def manEat(m):
    if isinstance(m,Man):   #判断m是否是Man类
        m.eat()        #多态调用，根据不同对象调用不同方法
    else:
        print("不能吃饭")

manEat(Chinese())

