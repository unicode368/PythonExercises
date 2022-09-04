global pos


def print_board():
    for i in range(n * n):
        if i % n == 0:
            print()
        print(board[i], end="\t")
    print()


def move():
    global pos
    direction = int(input("Enter the value please: \n1. UP - 8. \n2. DOWN - 2. "
                          "\n3. LEFT - 4. \n4. RIGHT - 6. \n5. EXIT - 5.\n"))
    while True:
        if direction == 2:
            if pos + n >= n**2:
                print("Can't move DOWN.")
                return 0
            board[pos] = 0
            board[pos + n] = 1
            pos += n
            return 0
        elif direction == 8:
            if pos - n < 0:
                print("Can't move UP.")
                return 0
            board[pos] = 0
            board[pos - n] = 1
            pos -= n
            return 0
        elif direction == 4:
            if pos - 1 < 0:
                print("Can't move LEFT.")
                return 0
            board[pos] = 0
            board[pos - 1] = 1
            pos -= 1
            return 0
        elif direction == 6:
            if pos + 1 < 0:
                print("Can't move LEFT.")
                return 0
            board[pos] = 0
            board[pos + 1] = 1
            pos += 1
            return 0
        elif direction == 5:
            return 1
        else:
            direction = int(input("Re-enter the value please: \n1. UP - 8. \n2. DOWN - 2. "
                                  "\n3. LEFT - 4. \n4. RIGHT - 6. \n5. EXIT.\n"))


n = int(input("Enter dimension:"))
board = [0] * (n ** 2)
board[n * (n - 1)] = 1
pos = n * (n - 1)
print("Initial board:")
print_board()

while True:
    if move() == 1:
        break
    else:
        print("After moving:")
        print_board()