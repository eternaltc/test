#测试单例

class MySingleton:

    __obj = None   #对象为空
    __init_flag = True   #标记

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)   #创建单例对象

        return cls.__obj

    def __init__(self,name):
        if MySingleton.__init_flag:    #保证只调用一次
            print("init....")
            self.name = name
            MySingleton.__init_flag = False     #false不执行

a = MySingleton("a")
b = MySingleton("b")
print(a)
print(b)


