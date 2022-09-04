# write the code
board = list(range(0, 9))
players = {'Player 1': 'X', 'Player 2': 'O'}
winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def is_winning_condition():
    for i in range(len(winning_positions)):
        if (board[winning_positions[i][0]] ==
                board[winning_positions[i][1]] == board[winning_positions[i][2]] == "X"):
            print("Player 1 won!")
            return
        elif (board[winning_positions[i][0]] ==
                board[winning_positions[i][1]] == board[winning_positions[i][2]] == "O"):
            print("Player 2 won!")
            return
    print("No matching.")


def print_desk():
    mul = 3
    for i in range(3):
        for j in range(3):
            print(board[j + i * mul], end="\t")
        print()


def make_move(player):
    pos = int(input(f"{player}, please enter position:"))
    if (pos < 0 or pos > 8) and type(board[pos]) != int:
        pos = int(input(f"This position doesn't exist or unavailable already. "
                        f"{player}, please re-enter position:"))
    board[pos] = players[player]


moves = 0
turn = 0
while moves < 9:
    print_desk()
    if turn % 2 == 0:
        make_move("Player 1")
    else:
        make_move("Player 2")
    turn += 1
    moves += 1
else:
    print_desk()
    is_winning_condition()