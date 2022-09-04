d = {'11': 'Diana', '12': 'Sarah'}
print(d.get('11'))

d = {10: 'ten', 20: 'twenty', 30: 'thirty'}
# since 42 is not in the keys, it'll print 'Not found'
print(d.get(42, "Not found"))  # if no such key - print the val
