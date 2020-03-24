#测试组合

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("骁龙")
        print("cpu对象",self)

class Screen:
    def show(self):
        print("猩猩屏幕")
        print("screen对象",self)

p = MobilePhone(CPU(),Screen())
p.cpu.calculate()
p.screen.show()