lst = [2, 3, 9, 8, 3, 1, 2, -40, 2]

minvalue = lst[0]
for elem in lst:
    # ask if that elem is the smallest we've seen so far
    # if it is the smallest, make it our new minimum
    if elem < minvalue:
        minvalue = elem
    
print(minvalue)
# print our minimum value
#print(minvalue)