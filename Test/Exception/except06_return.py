
def test01():
    try:
        a = 3/0
    except:
        print("异常，0不能做除数")
    finally:
        print("finlly")

    print("程序结束")
    return "e"  #return部放入try\except\else\finally中，放入方法最后

print(test01())

