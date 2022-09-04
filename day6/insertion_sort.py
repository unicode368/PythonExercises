a = [5, 4, 3, 2, 1, 0, 1, 2, 11, 6]

for i in range(len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print(a)
