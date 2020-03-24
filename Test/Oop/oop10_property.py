#测试@property

class Employee:

    @property
    def salary(self):
        print("salary  run")
        return 1000

e = Employee()
# e.salary()
print(e.salary)

# e.salary = 2000    不能设值