import math


def check_if_present(number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number //= 10
    return False


if __name__ == '__main__':
    n = int(input("Enter the number:"))
    while n < 0:
        n = int(input("Enter the number:"))
    len = int(math.log10(n))
    res = 0
    for i in range(1, len + 2):
        if not(check_if_present(res, n // 10**len)):
            res *= 10
            res += n // 10**len
        n %= 10**len
        len -= 1
    print(res)
