print("step0")
try:
    print("step1")
    a = 3/0
    print("step2为异常后面的代码")   #无异常继续执行，异常跳动执行exception
except BaseException as e:
    print("step3")
    print("异常为",e)
