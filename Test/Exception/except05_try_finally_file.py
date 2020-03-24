# try:
#     a = input("请输入一个被除数：")
#     b = input("请输入一个除数：")
#     c = float(a)/float(b)
#     # print(c)
# except BaseException as e:
#     print(e)
# else:
#     print(c)
# finally:
#     print("finally,无论是否发生异常，都执行")
# print("程序结束")

try:
    f = open("d:/a.txt","r")
    content = f.readline()
    print(content)
except:
    print("文件未找到")
finally:
    print("run in finally.关闭资源")
    try:
        f.close()
    except BaseException as e:
        print(e)

print("程序结束")




