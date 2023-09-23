number = int(input("enter a number:"))
if number<0:
    print("invalid number")
elif(number==0):
    print("factorial of 0 is", 1)
else:
    factorial = 1
    for i in range(1, number+1):
        factorial  = factorial*i
    print("factorial is", factorial)
