b = []
if not b:
    print("空列表是false")

c = True
if c:
    print("c=True")

c = ""
if not c:
    print("c=""是false")

c = "True"  #c="False"非空字符串打印
if c:
    print(c)

d = 0
if not d:
    print("d=0不打印")

m = 4
if 3<m<10:
    print("3<{}<10".format(m))

n = 20
if 3<n and (n==20):   #=报错
    print(n)
