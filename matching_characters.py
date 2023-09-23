stnc = input("enter any sentence/string:  ")
matchings_chart = set()
for i in stnc:
    if stnc.count(i)>1:
        matchings_chart.add(i)
print(matchings_chart)