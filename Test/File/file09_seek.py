with open("a.txt","r",encoding="utf-8") as f:
    print("文件名：",f.name)
    print(f.tell())
    print("读取的内容：{0}".format(f.readline()))
    print(f.tell())

    print("**********")
    f.seek(3)
    print("读取的内容：{0}".format(f.readline()))

