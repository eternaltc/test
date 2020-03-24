#文件拷贝
with open(r"E:\学习\python学习\1.png","rb") as f:
    with open("1_copy.png","wb") as w:
        for line in f.readlines():
            w.write(line)

print("图片拷贝完成")
