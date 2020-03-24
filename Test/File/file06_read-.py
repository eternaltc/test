print("****read(3)*****")
with open(r"file06.txt","r",encoding="utf-8") as f:
    str = f.read(3)  #中文和英文都是一个字符
    print(str)

print("****read()*****")
with open(r"file06.txt","r",encoding="utf-8") as f:
    s = f.read()
    print(s)

print("****readline()*****")
with open(r"file06.txt","r",encoding="utf-8") as f:
    s = f.readline()
    print(s)

print("****readlines*****")
with open(r"file06.txt","r",encoding="utf-8") as f:
    s = f.readlines()
    print(s)
