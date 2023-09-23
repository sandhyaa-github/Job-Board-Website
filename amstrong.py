n = int(input("enter a number:"))
len_of_n = len(str(n))
sum = 0
for i in str(n):
    sum = sum+int(i)**len_of_n
if sum == n:
    print("it's amstrong number,{}".format(n))
else:
    print("not an amstrong number {}".format(n))


