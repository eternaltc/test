#列表和字典存储表格的数据
tb = []
r1 = dict(name="高小一",age= 18,salary=3000,city="北京")
r2 = dict(name="高小二",age= 19,salary=2000,city="上海")
r3 = dict(name="高小三",age= 20,salary=1000,city="深圳")

tb = [r1,r2,r3]
for x in tb:
    if x.get("salary")>1500:
        print(x)