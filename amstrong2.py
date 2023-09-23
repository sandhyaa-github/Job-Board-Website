n = int(input("Enter a number:"))
original_n = n  # Store the original number to compare later
sum_of_powers = 0
num_digits = len(str(n))

while n > 0:
    digit = n % 10  # Extract the last digit
    sum_of_powers += digit ** num_digits
    n //= 10  # Remove the last digit

if sum_of_powers == original_n:
    print(f"{original_n} is an Armstrong number.")
else:
    print(f"{original_n} is not an Armstrong number.")