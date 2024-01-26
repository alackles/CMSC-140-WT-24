i = 0 
while i < 13:
    print("Bloody Mary!", i)
    i = i + 1
    print("Now i is", i)

print("---")

for i in range(0, 13):
    print("Bloody Mary", i)

mystring = "Hello everybody"
for index in range(len(mystring)):
    print(index)
    print(mystring[index])

for letter in mystring:
    print(letter)


list_of_nums = [1, 4, 5, 8, 9]
print("List:")
for i in list_of_nums:
    print(i)

print("Indexed:")
for i in range(len(list_of_nums)):
    print(i, list_of_nums[i])
print(i)
