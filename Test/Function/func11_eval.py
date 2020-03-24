
eval("print('abcdef')")   ##abcdef

s = "print('abcdef')"
eval(s)    #abcdef

a = 10
b = 20
c = eval("a+b") #a+b可以从web传进来
print(c)     #30

dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)    #指定执行dict1
print(d)      #300


