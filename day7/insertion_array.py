def display():
    if len(a) == 0:
        print("Nothing to display.")
    else:
        print("Current array: ", a, end="\n")

def find(key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return None


def insert(el, key, option):
    global a
    new_a = [0]*(len(a) + 1)
    insert_id = find(key)
    if insert_id is None:
        print("Element not found. Inserting in the end of the list...")
        a.append(el)
        return
    elif option == 1:
        for i in range(len(new_a)):
            if i == insert_id:
                new_a[i] = el
            elif i < insert_id:
                new_a[i] = a[i]
            else:
                new_a[i] = a[i - 1]
    elif option == 2:
        insert_id = find(key)
        for i in range(len(new_a)):
            if i == insert_id + 1:
                new_a[i] = el
            elif i < insert_id + 1:
                new_a[i] = a[i]
            else:
                new_a[i] = a[i - 1]
    a = new_a


a = []

while True:
    option = int(input("Please choose an option: \n1. Insert. \n2. Display. "
                       "\n3. EXIT.\n"))
    if option == 1:
        ele = int(input("Enter element:"))
        key = int(input("Enter data for element:"))
        pos = int(input("Please choose position for insertion: \n1. Before. \n2. After.\n"))
        insert(ele, key, pos)
    elif option == 2:
        display()
    elif option == 3:
        break
    else:
        option = int(input("Please re-enter the option: \n1. Insert. \n2. Display. "
                           "\n3. EXIT.\n"))