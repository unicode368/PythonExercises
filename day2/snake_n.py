n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))

# for any number there\'re 3 LINES ONLY. 3 conditions is a result of those
rows = 2 * n
cols = 4 * n - 2
for i in range(1,rows + 1):
    for j in range(1, cols + 1):
        if i + j == n + 1 or j - i == n - 1 or i + j == 5*n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()