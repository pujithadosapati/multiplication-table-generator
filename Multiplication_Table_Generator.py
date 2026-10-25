# Multiplication Table Generator
number = int(input("Enter a number: "))
limit = int(input("Enter the table limit: "))
print(f"\nMultiplication Table of {number}")
print("-" * 30)
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
