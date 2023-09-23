original_string = input("enter any string:")
rev_string = original_string[::-1]
reverse = ""
for i in original_string:
    reverse =i+reverse

print("original is {} and reversed is {}".format(original_string, rev_string), "----", reverse) 