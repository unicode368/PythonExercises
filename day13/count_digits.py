n = int(input("enter n = "))


def count(cnt, num):
    if num == 0:
        return cnt
    else:
        num //= 10
        cnt += 1
        return count(cnt, num)


counter = count(0, n)
print("Num of digits: ", counter)
