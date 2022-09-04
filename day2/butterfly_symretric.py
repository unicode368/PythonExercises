n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    mid = int(n / 2)
    add = 0
else:
    mid = int(n / 2) + 1
    add = 1

for i in range(1, n + 1):
    for j in range(n):
        if i + j > n - 1 and i - j <= 1:
            print("*", end="\t")
        elif i + j < n + 1 and i - j >= 1:
            print("*", end="\t")
        else:
            print(" ", end="\t")
    print()
