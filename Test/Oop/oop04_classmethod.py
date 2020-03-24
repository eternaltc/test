#测试类方法
class Staff:
    company = "OTC"  #类属性

    def __init__(self,name,age):  #实例方法
        self.name = name
        self.age = age

    @classmethod   #类方法
    def printCompany(cls):
        print(cls.company)
#       print(self.name)  #报错，类方法和静态方法中，不能调用实例变量、实例方法

Staff.printCompany()


