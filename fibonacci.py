num = int(input("enter n value:  "))
a,b = 0,1
count = 0
if num<0:
    print("enter a valid number")
elif num==1:
    print("fibonacci series is {}".format(1))
else:
    while count<num:
        print(a)
        nextElement = a+b
        a,b = b, nextElement
        count+=1

