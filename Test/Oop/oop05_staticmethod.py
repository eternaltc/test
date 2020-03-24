#测试静态方法
class Staff:
    company = "OTC"

    @staticmethod
    def add(a,b):  #静态方法
        print(Staff.company)
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b

Staff.add(2,3)
