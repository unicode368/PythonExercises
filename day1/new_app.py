def print_sums(n):
    output = []
    a = 0
    while a < n / 2:
        output.append(n - a)
        a += 1
        if a <= n / 2:
            output.append(a)
    print(output)


if __name__ == '__main__':
    n = int(input("Type number:"))
    while n < 0:
        n = int(input("Type number:"))
    print_sums(n)
