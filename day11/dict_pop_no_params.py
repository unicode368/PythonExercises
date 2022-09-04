# Python dictionary popitem() method removes last inserted
# key-value pair from the dictionary and returns it as a tuple
d = {10: 'Harvey', 2: 'Henry', 3: 'Brian'}
print(d.popitem())
print(d.popitem())
print(d.popitem())
# KeyError: 'popitem(): dictionary is empty'
print(d.popitem())