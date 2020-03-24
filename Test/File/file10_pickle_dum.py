import pickle

a1 = "陶垂"
a2 = 1234
a3 = [3,4,6,6]

with open("file10.data","wb") as f:   #文件后缀可以随便起
    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open("file10.data","rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1);print(b2),print(b3)

    print(id(a1));print(id(b1))    #id不一样，不是一个对象

