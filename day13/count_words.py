test_str = "if you are happy       that u got the job    .....  i appreciate your innocence fewe"


def count(ind=0):
    global counter
    if ind >= len(test_str):
        return
    while ind < len(test_str) and test_str[ind].isalpha():
        ind += 1
    if ind >= len(test_str):
        counter += 1
        return
    while ind < len(test_str) and not test_str[ind].isalpha():
        ind += 1
    counter += 1
    count(ind)


counter = 0
count()
print(counter)


