#测试lambda函数
f =lambda a,b,c,d:a+b+c+d
print(f(1,2,3,4))   #10

g = [lambda a:a*2,lambda b:b*2]
print(g[0](6))    #12
