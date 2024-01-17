# Write a program that takes a user's name and age as input and prints the year they were bornS

name = input("Enter your name: ")
age = input("Enter your age: ")
thisyear = input("Have you had your birthday this year? (Yes/No): ")
birthyear = 2024 - int(age)
if thisyear.lower() == "yes":
    birthyear = 2024 - int(age)
elif thisyear.upper() == "NO":
    birthyear = 2023 - int(age)
else: 
    print("Invalid input")
print("If you have had a birthday you were born in " + str(birthyear) +  ". Otherwise, you were born in", birthyear - 1)
print(name.upper())
print(age)
print(birthyear)