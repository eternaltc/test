#文本末尾加行号
with open("file07.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    lines = [temp.rstrip() + " #" + str(index+1)+"\n" for index, temp in enumerate(lines)]
    #python推导式

with open("file07.txt","w",encoding="utf-8") as f:
    f.writelines(lines)
