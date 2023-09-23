# Your list of integers (example)
input_list = [x for x in range(1,101) if x!=17 and x!=68]

reference_list = list(range(1, 101))

# Use set difference to find the missing numbers
missing_numbers = list(set(reference_list) - set(input_list))

print("Missing numbers:", missing_numbers)
