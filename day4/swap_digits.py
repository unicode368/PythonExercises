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
start = 0

if length % 2 != 0:
    res += n % 10
    n //= 10
    start += 1
for i in range(start, length, 2):
    first_num = n % 10
    second_num = n % 100 // 10
    res += second_num * 10**i
    res += first_num * 10**(i + 1)
    n //= 100
print(res)


