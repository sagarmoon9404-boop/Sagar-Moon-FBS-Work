# take input
num = int(input("Enter a 3-digit number: "))

# perform operation
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Reverse the number
reverse = ones * 100 + tens * 10 + hundreds

if num == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
