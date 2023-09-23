name1, name2 = input("enter string1: ", ),  input("enter string2: ", )
if len(name1)==len(name2):
    if sorted(name1)==sorted(name2):
        print("these are anagrams")
    else:
        print("lenght is same but these are not anagrams")
else:
    print("not anagrams")