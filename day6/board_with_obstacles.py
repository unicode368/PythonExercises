import random


def place_borders():
    for i in range(4, 7):
        board[i] = 'X'
    for i in range(3):
        board[i + 14] = 'X'
    board[19] = 'X'
    board[20] = 'X'
    board[28] = 'X'
    for i in range(3, 7):
        board[i + 28] = 'X'
    for i in range(3):
        board[i + 42] = 'X'


def make_move(player1, player2):
    direction = random.randrange(1, 5)
    dice = random.randrange(1, 7)
    if direction == 1:
        # UP
        if players[player1] - dice * 7 < 0:
            players[player1] = 0
        elif board[players[player1] - dice * 7] == 'X':
            players[player1] = 0
        elif type(board[players[player1] - dice * 7]) != int and board[players[player1] - dice * 7] == player2:
            players[player1] -= dice * 7
            players[player2] = 0
        else:
            players[player1] -= dice * 7
    elif direction == 2:
        # DOWN
        if players[player1] + dice * 7 >= len(board):
            players[player1] = 0
        elif board[players[player1] + dice * 7] == 'X':
            players[player1] = 0
        elif type(board[players[player1] + dice * 7]) != int and board[players[player1] + dice * 7] == player2:
            players[player1] += dice * 7
            players[player1] = 0
        else:
            players[player1] += dice * 7
    elif direction == 3:
        # LEFT
        if players[player1] - dice <= (players[player1] // 7) * 7 or players[player1] - dice < 0:
            players[player1] = 0
        elif board[players[player1] - dice] == 'X':
            players[player1] = 0
        elif type(board[players[player1] - dice]) != int and board[players[player1] - dice] == player2:
            players[player1] -= dice
            players[player2] = 0
        else:
            players[player1] -= dice
    else:
        # RIGHT
        if players[player1] + dice >= (players[player1] // 7 + 1) * 7 or players[player1] + dice >= len(board):
            players[player1] = 0
        elif board[players[player1] + dice] == 'X':
            players[player1] = 0
        elif type(board[players[player1] + dice]) != int and board[players[player1] + dice] == player2:
            players[player1] += dice
            players[player2] = 0
        else:
            players[player1] += dice
    print(players[player1], " ", players[player2])


def print_board():
    for i in range(len(board)):
        if i % 7 == 0:
            print()
        if players["A"] == players["B"] == i == 0:
            print("A,B", end="\t")
        elif players["A"] == i:
            print("A", end="\t")
        elif players["B"] == i:
            print("B", end="\t")
        else:
            print(board[i], end="\t")


board = [0]*(7 ** 2)
players = {"A": 0, "B": 0}
a_score = 0
b_score = 0
turn = 0

place_borders()

while players["A"] != 48 or players["B"] != 48:
    print_board()
    print()
    if turn % 2 == 0:
        make_move("A", "B")
    else:
        make_move("B", "A")
    turn += 1



