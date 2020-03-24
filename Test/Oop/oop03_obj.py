class Staff:
    company = "OTC"  #类属性
    count = 0      #类属性

    def __init__(self,name,id):
        self.name = name
        self.id = id
        Staff.count = Staff.count + 1

    def say(self):
        print("{0}的公司是：{1}".format(self.name,Staff.company))
        print(self.name,"的工号是：",self.id)

s1 = Staff("陶垂","A01110")
s1.say()

s2 = Staff("对三","123")
s3 = Staff("王炸","1")
print("一共创建{0}个Staff对象".format(Staff.count))
