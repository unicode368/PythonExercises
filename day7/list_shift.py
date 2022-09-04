n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)

shift = int(input("Enter shift val = "))

shift = shift % n
start_ind = -(n - shift)

c = [0]*n
j = 0

for i in range(start_ind, start_ind + n):
    c[j] = a[i]
    j += 1

print(c)
