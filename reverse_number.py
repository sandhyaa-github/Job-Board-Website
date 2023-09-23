n = int(input("enter any number:  "))
reverse = 0
num = n
while n>0:
    last_digit = n%10
    reverse = reverse*10+last_digit
    n//=10
print(reverse)