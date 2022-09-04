def fun(n):
    if n == 0:
        return 0
    return 1 + fun(n // 10)


def fun1(n, cnt=0):
    if n == 0:
        return cnt
    return fun1(n // 10, cnt + 1)


n = int(input("Enter the num = "))
print("count of dig = ", fun(n), fun1(n))
