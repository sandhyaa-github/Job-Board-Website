num = int(input("enter any number:   "))
factors_list = []
for i in range(1, num+1):
    if (num%i==0):
        factors_list.append(i)

print("factors of {} is {}".format(num, factors_list))

