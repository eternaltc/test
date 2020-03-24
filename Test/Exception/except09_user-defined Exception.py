
class AgeError(Exception):  #继承Exception
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo)+"年龄错误,应该为0-150"


if __name__ =="__main__":   #如果为True,则模块作为独立文件运行测试代码
    age = int(input("输入年龄："))
    if age<0 or age>150:
        raise AgeError(age)
    else:
        print("年龄为：",age)


