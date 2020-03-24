#测试私有属性

class Employee:
    __company = "OTC"
    def __init__(self,name,age):
        self.name = name
        self.__age = age   #私有属性

    def __work(self):   #私有方法
        print("好好工作")
        print("年龄：{0}".format(self.__age))      #内部调用
        print("公司：{0}".format(Employee.__company))

e = Employee("陶垂",18)
print(e.name)
print(e._Employee__age)    #外部调用私有属性
e._Employee__work()         #外部调用私有方法
print(Employee._Employee__company)


