master = []
properties = set()
while True:
    key = input("Enter the property = ")
    value = input("Enter the value = ")
    master.append([key, value])
    properties.add(key)
    ch = int(input("Press 1 to continue..."))
    if ch != 1:
        break
print(master)
print("Unique features = ", properties)