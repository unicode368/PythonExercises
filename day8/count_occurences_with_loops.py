list = [1, 2, 11, 2, 5, 3, 5, 1, 3, 3, 11, 8, 7, 6]

count = 0
while len(list) > 0:
    el = list[0]
    for i in range(len(list)):
        if el == list[i - count]:
            del list[i - count]
            count += 1
    print(f"Element {el} occurrences - {count}")
    count = 0
