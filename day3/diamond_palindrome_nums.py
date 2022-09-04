n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
col = 2*n - 1
row = 2*n - 1
mid = n
it = 1

for i in range(1, row + 1):
    if n > i:
        print("\t" * (n - i), end="")
    else:
        print("\t" * (i - n), end="")
    j = 1
    it = 1

    while (i >= j and it > 0) or (j >= 1 and it < 0):
        print(j, end="\t")
        if (j < i <= n) or ((2 * n - 1) - i >= j and i > n):
            j += it
        else:
            j -= 1
            it = -1
    if n > i:
        print("\t" * (n - i), end="")
    else:
        print("\t" * (i - n), end="")
    print()
