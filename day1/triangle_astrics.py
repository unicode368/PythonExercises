n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    len = int(n / 2)
else:
    len = int(n / 2) + 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i <= len and (j == 1 or j == i):
            print("*", end="")
        else:
            if (n - i + 1 - j) < 0:
                break
            if j == 1 or (n - j + 1) <= i:
                print("*", end="")
            else:
                print(" ", end="")
    print()