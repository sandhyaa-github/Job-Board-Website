string = input("enter any string:")
if(string == string[::-1]):
    print("yes, {} is palindrome".format(string))
else:
    print('{} is not a palindrom'.format(string))