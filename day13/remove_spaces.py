test_str = "if you are happy       that u got the job    .....  i appreciate your innocence"
new_str = ""


def remove_spaces(ind=0):
    global new_str
    if ind >= len(test_str):
        return
    while ind < len(test_str) and test_str[ind] != " ":
        new_str += test_str[ind]
        ind += 1
    if ind >= len(test_str):
        return
    i = 0
    while ind < len(test_str) and test_str[ind] == " ":
        if i == 0:
            new_str += test_str[ind]
            i += 1
        ind += 1
    remove_spaces(ind)


remove_spaces()
print(new_str)
