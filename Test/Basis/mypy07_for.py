for x in (1,2,3,4):
    print(x*3,end=" ")

for y in "abcefghijklmnopqrstuv":
    print(y,end="")

print()
print("***********************")

d = {"name":"tc","age":18,"job":"IT"}
for x in d:
    print(x,end="\t")  #打印键

print()
for x in d.keys(): #返回键
    print(x,end="\t")

print()
for x in d.values():  #返回值
    print(x,end="\t")

print()
for x in d.items(): #返回键值对
    print(x,end="\t")