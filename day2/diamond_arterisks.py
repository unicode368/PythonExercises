n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    len = int(n / 2)
else:
    len = int(n / 2) + 1

for i in range(1, n + 1):
    for j in range(1,n + 1):
        if n % 2 != 0 and (i + j <= len or i - j >= len or j - i >= len or i + j >= n + len + 1):
            print("*\t", end="")
        elif n % 2 == 0 and (i + j <= len or i - j >= len + 1 or j - i >= len + 1 or i + j >= n + len + 2):
            print("*\t", end="")
        else:
            print("-\t", end="")
    print()