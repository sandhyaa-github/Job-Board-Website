list1 = [-50,3,67,8,8,0,90,91,98]
small= list1[0]
large = list1[0]
for i in range(1, len(list1)):
    if list1[i]>small:
        large = list1[i]
    if small>list1[i]:
        small = list1[i]
print(small, large)
