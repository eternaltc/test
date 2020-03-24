s = ["陶垂\n","123","456"]
with open(r"file05.txt","w",encoding="utf-8") as f:
    f.writelines(s)
    f.write("i love you")

