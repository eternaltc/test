
import csv
with open("test1.csv","r") as f:
    a_csv = csv.reader(f)   #读
   # print(list(a_csv))    #如果打印该句，后面的不能打印，指针已指到最后
    for row in a_csv:
        print(row)

with open("test01.csv","w") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["ID","姓名","年龄"])  #写入一行
    b_csv.writerow(["11","陶垂","18"])

    c = [["1","ONE","1"],["2","TWO","2"]]
    b_csv.writerows(c)   #全部写入


