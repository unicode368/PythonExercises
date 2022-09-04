n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))

for i in range(n + 1, 1, -1):
    if i % 2 != 0:
        for j in range(1, i):
            print(j, end="")
    else:
        for j in range(i, 1, -1):
            print(j - 1, end="")
    print()