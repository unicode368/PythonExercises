a = [11, 22, 33, 44]
b = [1, 2, 3]


def get_len(a):
    count = 0
    for i in a:
        count += 1
    return count


len_a = get_len(a)
n = len_a + get_len(b)
c = [0]*n

for i in range(n):
    if i >= len_a:
        c[i] = b[i - len_a]
    else:
        c[i] = a[i]

print(c)

