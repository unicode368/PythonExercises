from player import Player
from graphics import Graphics
import random

board = []
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
turns_and_players = {1: player1, 2: player2, 3: player3, 4: player4}
safe_pos = [(2, 0), (4, 2), (2, 4), (0, 2)]


def init_board():
    global board
    for i in range(5):
        row = []
        for j in range(5):
            row.append((i, j))
        board.append(row)


def init_players():
    global player1, player2, player3, player4
    player1.set_player((4, 2), Graphics.SUITS[0], Graphics.COLORS[0], (4, 1))
    player2.set_player((2, 4), Graphics.SUITS[1], Graphics.COLORS[1], (3, 4))
    player3.set_player((0, 2), Graphics.SUITS[2], Graphics.COLORS[2], (0, 3))
    player4.set_player((2, 0), Graphics.SUITS[3], Graphics.COLORS[3], (1, 0))


def update_board():
    pass


def check_position(pos):
    global player1, player2, player3, player4
    res = []
    if pos in player1.coins.values():
        res.append(("player1", player1.count_coins_in_pos(pos)))
    if pos in player2.coins.values():
        res.append(("player2", player2.count_coins_in_pos(pos)))
    if pos in player3.coins.values():
        res.append(("player3", player3.count_coins_in_pos(pos)))
    if pos in player4.coins.values():
        res.append(("player4", player4.count_coins_in_pos(pos)))
    return res


def print_board():
    for i in range(5):
        for j in range(5):
            curr_pos = check_position((i, j))
            if curr_pos == []:
                print("\033[90m", "\033[1m", Graphics.EMPTY_POS, end="\t")
            elif curr_pos[0][0] == "player1":
                print(player1.color + player1.coin_avatar, curr_pos[0][1], end="\t")
            elif curr_pos[0][0] == "player2":
                print(player2.color + player2.coin_avatar, curr_pos[0][1], end="\t")
            elif curr_pos[0][0] == "player3":
                print(player3.color + player3.coin_avatar, curr_pos[0][1], end="\t")
            elif curr_pos[0][0] == "player4":
                print(player4.color + player4.coin_avatar, curr_pos[0][1], end="\t")
        print()


def check_game_end_condition():
    global player1, player2, player3, player4
    return player1.winning_order is not None and \
           player2.winning_order is not None and \
           player3.winning_order is not None and \
           player4.winning_order is not None

def is_safe_pos(pos):
    if pos in safe_pos:
        return True


def make_move(player, dice_val, turn):
    curr_coin_pos = player.coins[player.curr_coin]
    move_count = 1
    new_row_pos = curr_coin_pos[0]
    new_col_pos = curr_coin_pos[1]

    while move_count <= dice_val:
        if (new_row_pos, new_col_pos) == player.stop_position:
            if move_count < dice_val and player.curr_coin != "c4":
                print("Player stuck...")
                player.set_curr_coin()
                print(player.curr_coin)
                curr_coin_pos = player.coins[player.curr_coin]
                new_row_pos = curr_coin_pos[0]
                new_col_pos = curr_coin_pos[1]
                move_count = 1
            elif move_count == dice_val:
                break
        elif (new_row_pos, new_col_pos) == player.stop_position and \
                move_count != dice_val and player.curr_coin == "c4":
            return
        elif new_col_pos == player.boundaries[1] \
                and new_row_pos != player.boundaries[2]:
            new_row_pos += 1
        elif new_row_pos == player.boundaries[2] and \
                new_col_pos != player.boundaries[3]:
            new_col_pos += 1
        elif new_col_pos == player.boundaries[3] and \
                new_row_pos != player.boundaries[0]:
            new_row_pos -= 1
        elif new_row_pos == player.boundaries[0] and \
                new_col_pos != player.boundaries[1]:
            new_col_pos -= 1
        move_count += 1
    new_pos_player = check_position((new_row_pos, new_col_pos))
    if is_safe_pos((new_row_pos, new_col_pos)):
        print("safe spot!")
        player.set_coins(player.curr_coin, (new_row_pos, new_col_pos))
    else:
        player.set_coins(player.curr_coin, (new_row_pos, new_col_pos))
        is_killed = False
        for player_in_the_spot in new_pos_player:
            if new_pos_player != [] and int(player_in_the_spot[-1]) != turn:
                killed_player = turns_and_players[int(player_in_the_spot[-1])]
                for i in killed_player.coins.keys():
                    if killed_player.coins[i] == (new_row_pos, new_col_pos):
                        is_killed = True
                        killed_player.coins[i] = killed_player.init_pos
        if is_killed:
            print("Someone gets killed!")


init_board()
init_players()
print("The game begins!")
turn = 1

while not check_game_end_condition():
    print()
    print_board()
    print()
    dice = random.randint(1, 4)
    print("Dice value: ", dice)
    print(f"It's player{turn} move")
    if turn == 1:
        make_move(player1, dice, turn)
    elif turn == 2:
        make_move(player2, dice, turn)
    elif turn == 3:
        make_move(player3, dice, turn)
    else:
        make_move(player4, dice, turn)
    if turn == 4:
        turn = 1
    else:
        turn += 1
    cont = input("Enter something to continue...")
