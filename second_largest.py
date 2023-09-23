list1 = [-50,3,67,8,8,0,90,91,98]
fm = max(list1[0], list1[1])
sm = min(list1[0], list1[1])

for i in range(2, len(list1)):
    if (list1[i]>fm):
        sm = fm
        fm = list1[i]
    elif(list1[i]>sm):
        sm = list1[i]
print(sm, fm)
