n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))

n_square = n**2

while n > 0:
    if n % 10 != n_square % 10:
        print(False)
        break
    else:
        n //= 10
        n_square //= 10
if n == 0:
    print(True)
