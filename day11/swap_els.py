els = [-1, 333, 2, 44, 1, 66, 777]
inserted = False

i = 0
while i < len(els):
    j = 2
    while i + j < len(els):
        if els[i] > els[i + j]:
            els[i], els[i + j] = els[i + j], els[i]
        j += 2
    i += 1


print(els)
