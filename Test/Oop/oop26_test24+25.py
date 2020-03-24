#测试单例

class CarFactory:
    def create_car(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()

    __obj = None   #对象为空
    __init_flag = True   #标记

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)   #创建单例对象

        return cls.__obj

    def __init__(self):
        if CarFactory.__init_flag:    #保证只调用一次
            print("init CarFactory....")
            CarFactory.__init_flag = False     #false不执行

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1 = factory.create_car("奔驰")
c2 = factory.create_car("比亚迪")

print(c1)
print(c2)


factory2 = CarFactory()
c1 = factory2.create_car("奔驰")
c2 = factory2.create_car("比亚迪")

print(c1)
print(c2)

