
class A:
    def aa(self):
        print("aa")
    def say(self):
        print("AA")

class B:
    def bb(self):
        print("bb")
    def say(self):
        print("BB")

class C(B,A):
    def __init__(self,nn):
        self.nn = nn
    def cc(self):
        print("cc")


c = C(3)
c.cc()
c.bb()
c.aa()

print(C.mro())   #打印类的层次结构
c.say()         #从左到右的方式寻找，会执行B中的say()

print("************************************************")
print("c类的层次结构",C.mro())   #打印类的层次结构
print("c对象属性",dir(c))     #对象属性
print("c对象的属性字典",c.__dict__) #对象的属性字典
print("c对象所属的类",c.__class__)  #对象所属的类
print("C类的基类",C.__bases__)  #类的基类
print("A的子类列表",A.__subclasses__())  #A的子类列表


