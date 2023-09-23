name = input("enter a string: ")
character = input("give any character:  ")
if character in name:
    print(name.count(character))
else:
    print("character is not there")
count=0
for i in name:
    if character==i:
        count+=1
print(count)