n = int(input("Enter n:"))

row = col = 2 * n+1
s = str(n)*row

for i in range(1, row+1):
    print(s)
    if i < n:
        s = s[:i] + str(n-i)*(row-2*i) + s[-i:]
    elif i>=n and i<n+2:
        continue
    else:
        s = s[:(row - i)] + str(i - n)*(i - n) + str(i - n - 1)*(i - n - 1) + s[-(row - i):]
if n == 1:
    print("  1")

