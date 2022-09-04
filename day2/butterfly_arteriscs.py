n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    mid = int(n / 2)
else:
    mid = int(n / 2) + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if mid > i >= j or (i == mid and ((j <= mid and n % 2 == 0) or n % 2 == 1)):
            print("*\t", end="")
        elif i > mid:
            if mid % 2 == 0 and j >= i:
                print("*\t", end="")
            elif mid % 2 != 0 and j >= i:
                print("*\t", end="")
            else:
                print(" \t", end="")
    print()