def get_length(n):
    len = 0
    while n > 0:
        len += 1
        n //= 10
    return len


n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
length = get_length(n)
res = 0
temp = n
for i in range(1, length + 1):
    res += (temp % 10)**length
    temp //= 10
if res == n:
    print("is Armstrong number")
else:
    print("not Armstrong number")
