import random

# the list that is holding matrix positions
board = [(2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (2, 2)]


# returns current position of player
def get_pos(player):
    for board_i in range(1, len(board)):
        if player[0] == board[board_i][0] and \
                player[1] == board[board_i][1]:
            return board_i
    return 0


# returns matrix position which corresponds to index of list
def get_board_pos(pos):
    return board[pos]


# illustrates the board and position of players on it
def gen_board():
    for i in range(1, len(board) // 3 + 1):
        for j in range(1, len(board) // 3 + 1):
            tuple = (i, j)
            if get_pos(S) == get_pos(O) == board.index(tuple) == 0:
                print("V, S", end='\t')
            elif get_pos(S) == get_pos(tuple):
                print("V", end='\t')
            elif get_pos(O) == get_pos(tuple):
                print("S", end='\t')
            else:
                print(board.index(tuple), end='\t')
        print()


# init vars
dice_val = 0  # dice value
S = (2, 1)  # player1 position (Velma)
O = (2, 1)  # player2 position (Shaggy)
next_turn = False  # check whose turn it is

print("THE GAME BEGINS!1!1")
# play the game until some wins => enters (2,2) position
while not (S == (2, 2) or O == (2, 2)):
    gen_board()
    dice_val = random.randrange(1, 4)  # rolling the dice
    if not next_turn:  # checking if it's Velma's turn
        if get_pos(S) == 6 and dice_val == 3:  # if Velma in position 6 and dice_val is 3 - skip the turn
            print("Velma skips the turn.")
        elif get_pos(S) == 7 and dice_val > 1:  # if Velma in position 7 and dice_val > 1 - skip the turn
            print("Velma skips the turn.")
        else:
            next_position = get_board_pos((get_pos(S) + dice_val) % len(board))  # calculate new position
            print("Velma moves from {}".format(get_pos(S)), "to {}".format(get_pos(next_position)))
            S = next_position  # assign new position to Velma
            if S == O != board[0]:  # if Velma's position is the same as Shaggy's - press F for Shaggy
                print("JEENKIES!1!Velma killed Shaggy. Brute!")
                O = board[0]  # Shaggy is returning to safe place
    else: # executes if it's Shaggy's turn
        if get_pos(O) == 6 and dice_val == 3:  # if Shaggy in position 6 and dice_val is 3 - skip the turn
            print("Shaggy skips the turn.")
        elif get_pos(O) == 7 and dice_val > 1:  # if Shaggy in position 7 and dice_val > 1 - skip the turn
            print("Shaggy skips the turn.")
        else:
            next_position = get_board_pos((get_pos(O) + dice_val) % len(board))  # calculate new position
            print("Shaggy moves from {}".format(get_pos(O)), "to {}".format(get_pos(next_position)))
            O = next_position  # assign new position to Shaggy
            if S == O != board[0]:  # if Shaggy's position is the same as Velma's - press F for Shaggy
                print("ZOINKS!1!Shaggy killed Velma. Brute!")
                S = board[0]  # Velma is returning to safe place
    next_turn = not next_turn  # change the turn

if S == (2, 2):  # if Velma is in (2,2) position
    print("Velma wins!")
else:  # Shaggy is in (2,2) position
    print("Shaggy wins!")
print("GAME OVER. Here's your Scooby Snack")
