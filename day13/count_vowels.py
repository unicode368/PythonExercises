str = input("Please, enter the string:")


def count(ind=0):
    if ind >= len(str):
        return 0
    elif str[ind].lower() in "auioe":
        return 1 + count(ind + 1)
    return count(ind + 1)


res = count()
print(res)
