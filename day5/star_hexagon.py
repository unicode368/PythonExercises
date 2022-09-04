n = input("Enter the word:")

row = len(n) if len(n) % 2 != 0 else len(n) + 1
letters = list(n)
cols = len(n) + 2
mid = row // 2 + 1 if row % 2 != 0 else row // 2
edge = 3 if len(n) % 2 != 0 else 2

for i in range(1, row + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == row:
            print("\t" * ((cols - edge) // 2), "*\t" * edge,
                  "\t" * ((cols - edge) // 2), end="\t")
            break
        elif i == mid and (j == 1 or j == cols):
            print("*", end="\t")
        elif i == mid and 2 <= j < cols:
            print(letters[j - 2], end="\t")
        elif ((i + j) == mid + 1 and j != 0 and i <= mid) or \
                ((i + j) == mid + cols and j != 0 and i >= mid):
            print("*", end="\t")
        elif ((i - j) == row // 2 and j != 0 and i > mid) or \
                (j - i) == (mid + 1 if len(n) % 2 != 0 else mid) and j != 0 and i < mid:
            print("*", end="\t")
        else:
            print(" ", end="\t")
    print()
