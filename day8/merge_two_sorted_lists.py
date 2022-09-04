a = [11, 22, 33, 44, 55]
b = [30, 33, 36]
c = []

i = 0
j = 0

while i < len(a) or j < len(b):
    if i >= len(a):
        c.append(b[j])
        j += 1
    elif j >= len(b):
        c.append(a[i])
        i += 1
    elif a[i] == b[j]:
        c.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        c.append(a[i])
        i += 1
    elif a[i] > b[j]:
        c.append(b[j])
        j += 1

print(c)
