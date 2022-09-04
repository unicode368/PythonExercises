def printme(s, ind=-1):
    if ind < -(len(s)):
        return
    print(s[ind], end="")
    printme(s, ind - 1)


s = "apple is a fruit"
printme(s)
