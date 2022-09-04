n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))

row = n * 2
col = n * 2 - 1
mid = n

for i in range(1, row + 1):
    for j in range(1,col + 1):
        if j == 1 or j == col:
            print("*", end="\t")
        elif i == 1 or i == row:
            print("*", end="\t")
        elif j <= mid and i + j <= n + 1:
            print("*", end="\t")
        elif j > mid and i + (col - j) < n + 1:
            print("*", end="\t")
        else:
            print(" ", end="\t")
    print()