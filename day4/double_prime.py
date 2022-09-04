def check_if_prime(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


n = int(input("Enter the number:"))
digits_sum = 0

if check_if_prime(n):
    while n > 0:
        digits_sum += n % 10
        n //= 10

    print(check_if_prime(digits_sum))
else:
    print(False)
