
#字典推导式,统计字符出现的次数
# my_text = "I love you,tc,I love you"
# char_count = {c:my_text.count(c) for c in my_text}
# print(char_count)


#一般方式for循环推导作业
my_text = "I love you,tc,I love you"

for a in my_text:
    count = my_text.count(a)
    # char = {my_text[:],count}
    # print(char)
    char_count = {a,count}
    print(char_count)
    print("{0}:{1}".format(a,count),end="\t")