try:
    f = open(r"file04.txt","a")
    s = "tc"
    f.write(s)
except BaseException as e:
    print(3)
finally:
    f.close()

