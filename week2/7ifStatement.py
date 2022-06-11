# if condition

print("Please enter your Date your birth")

birth_year = int(input())

current_year = 2021

age = current_year - birth_year

if (age < 13):
    print("You are not allowed.")
else:
    print("You are allowed")

print("Have a nice time")