n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
max = n
n -= 1
it = -1

while n != max:
    if n == -1:
        n += 2
        it = 1
    else:
        print(n + 1, end=" ")
        n += it
