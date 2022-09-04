test_dict = {'111': {'name': 'Abas', 'salary': 100000}}

# printing original dictionary
print("The original dictionary is: ", test_dict)

# using nested get() Safe access nested dictionary key
res = test_dict.get('111', {}).get('name')

# printing result
print("The nested safely accessed value is : " + str(res))

res = test_dict.get('111', {}).get('salary')
print("The nested safely accessed value is : " + str(res))
