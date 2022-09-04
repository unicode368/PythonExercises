def insert(ele):
    global a
    if len(a) == 0:
        a.append(ele)
        return
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if a[mid] >= ele > a[mid - 1]:
            break
        elif a[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    if a[mid] < ele and mid == len(a) - 1:
        a = a + [ele]
    else:
        a = a[:mid] + [ele] + a[mid:]


a = []
while True:
    ele = int(input("Enter the ele = "))
    insert(ele)
    print(a)
