# initializing dictionary
test_dict = {"Josh": 7, "Olha": 1, "Aryan": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_first = test_dict.pop("Olha")

# Printing the value associated to popped key
print("Value associated to popped key is " + str(pop_first))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))