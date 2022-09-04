# given dictionary
dict1 = {10: 'a', 20: [1, 2, 3], 30: 'c'}
print("Given dictionary : ", dict1)
# new dictionary and copying using copy() method
dict2 = dict1.copy()
print("New copy : ", dict2)

# Updating dict2 elements and checking the change in dict1
dict2[10] = 10
dict2[20][2] = '45'  # list item updated
print("After updating the 2nd element in key = 20 ")
print("Original     :", dict1)
print("Updated copy :", dict2)
# array is shared between dict1 and dict2!!!
