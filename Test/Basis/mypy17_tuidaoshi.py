
#列表推导式
print("***测试1***")
y = [x for x in range(5)]
print(y)

y = [x*2 for x in range(20) if x%5==0]
print(y)

print("***测试2：for循环实现***")
y = []
for x in range(20):
    if x%5==0:y.append(2*x)
print(y)

print("***双层循环***")
cells = [(row,col) for row in range(10) for col in range(10)]
print(cells)

#字典推导式,统计字符出现的次数
my_text = "I love you,tc,I love you"
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

#集合推导式
b = {x for x in range(1,100) if x%9==0}
print(b)

#生成器推导式
gnt = (x for x in range(4))
print(tuple(gnt))
print(tuple(gnt))  #第二次就没有了

gnt = (x for x in range(4))
for x in gnt:  #gnt是生成器对象，生成器是克迭代对象,只能使用一次
    print(x,end=",")
print("************")
print(tuple(gnt))
