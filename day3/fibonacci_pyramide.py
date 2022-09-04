
def fibterm(term):
    n1 = 0
    n2 = 1
    if term == 1:
        print(n1, end="\t")
    elif term == 2:
        print(n1+n2, end="\t")
    else:
        cnt = 2
        while cnt<term:
            n3=n1+n2
            n1=n2
            n2=n3
            cnt+=1
        else:
            print(n3, end="\t")


n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))

row = n
col = 2*n - 1
mid = n

prev = 0
cur = 1
cnt = 1

for i in range(1, row + 1):
    print("\t" * (row - i), end="")
    for j in range(2*i - 1):
        fibterm(cnt)
        cnt += 1
    print("\t" * (row - i), end="")
    print()
