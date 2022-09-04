original = {1: 'Anna', 2: 'Martin'}

# using copy() method
new = original.copy()

new.clear()

print("new: ", new)
print("original: ", original)

original = {10: "Medical", 2: "Mechanical", 3: "Electronics"}
# using '=' operator
new = original
new.clear()
print("new: ", new)
print("original: ", original)

