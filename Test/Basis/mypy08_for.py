#累加，偶数和，奇数和
sum_all = 0
sum_odd = 0
sum_even = 0
for i in range(101):
    sum_all += i
    if i%2==0:
        sum_odd +=i
    else:
        sum_even +=i
print("1-100累加{0}，奇数和{1}，偶数和{2}".format(sum_all,sum_odd,sum_even))
