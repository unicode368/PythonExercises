n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    len = int(n / 2)
else:
    len = int(n / 2) + 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i <= len:
            print(j, end="")
        else:
            if (n - i + 1 - j) < 0:
                break
            print(j, end="")
    print()
