#列表内容修改
a = ["我喜欢你\n","很喜欢\n","nice\n"]
b = enumerate(a)  #枚举，变成元组
print(a)
print(list(b))

c = [temp+" #"+str(index) for index,temp in enumerate(a)]
#temp 表示元组内容    index：元组序号
print(c)

d = [temp.rstrip()+" #"+str(index) for index,temp in enumerate(a)]
#temp 表示元组的内容    index：元组序号
print(d)


