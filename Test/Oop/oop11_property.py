
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("录入错误，薪水在1000-5000")

'''
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("录入错误，薪水在1000-5000")

e = Employee("陶垂",10000)
print(e.get_salary())
e.set_salary(-2000)    #输入
print(e.get_salary())
'''
e = Employee("陶垂",10000)
print(e.salary)
e.salary = -2000
print(e.salary)