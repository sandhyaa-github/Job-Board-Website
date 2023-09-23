string1 = input("enter any string:  ")
digits = ['0','1','2','3','4','5','6','7','8','9']
count = 0
for i in string1:
    #if i.isdigit():
    if i in digits:

        count+=1
print(count)

