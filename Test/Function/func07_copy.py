#测试浅拷贝、深拷贝
import copy

def copyTest():
    a = [1, 2, [3, 4]]
    b = copy.copy(a)
    print("a", a)
    print("b", a)

    print("浅拷贝...........")
    b.append(5)
    b[2].append(7)  # 浅拷贝只拷贝字对象的引用a,改变子对象里面的值
    print("a", a)
    print("b", b)

def deepCopyTest():
    a = [1, 2, [3, 4]]
    b = copy.deepcopy(a)

    print("深拷贝...........")
    b.append(5)
    b[2].append(7)  #深拷贝，拷贝所有
    print("a", a)
    print("b", b)

copyTest()
deepCopyTest()