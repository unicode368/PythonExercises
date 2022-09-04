#needs improvement
n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
len = n * 2
for j in range(1, n + 1):
    for i in range(1, len):
        if i <= j:
            print(str(i), end="")
        elif j >= len - i:
            print(str(len - i), end="")
        elif i - 1 == j:
            print(" "*((len - 1) - 2 * j), end="")
    print()
