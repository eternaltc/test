
class A:
    def say(self):
        print("A",self)

class B(A):
    def say(self):
        A.say(self)      #获得父类的定义
        super().say()    #获得父类的定义
        print("B", self)

B().say()

