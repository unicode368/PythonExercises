class Player:

    def __init__(self):
        self.have_killed = False
        self.init_pos = ()
        self.coins = {}
        self.coin_avatar = None
        self.color = ""
        self.winning_order = None
        self.stop_position = (0, 0)
        self.curr_coin = ""
        self.boundaries = [0, 0, 4, 4]

    def set_player(self, init_pos, coin_avatar, color, stop_pos):
        self.have_killed = False
        self.init_pos = init_pos
        self.coins = {"c1": init_pos, "c2": init_pos,
                      "c3": init_pos, "c4": init_pos}
        self.coin_avatar = coin_avatar
        self.color = color
        self.winning_order = None
        self.stop_position = stop_pos
        self.curr_coin = "c1"
        self.boundaries = [0, 0, 4, 4]

    def set_have_killed(self):
        self.have_killed = True
        self.stop_position = None

    def set_curr_coin(self):
        self.curr_coin = "c" + str(int(self.curr_coin[1]) + 1)

    def set_boundaries(self, boundaries):
        self.boundaries = boundaries

    def set_winning_order(self, order):
        self.winning_order = order

    def set_coins(self, coin_id, new_pos):
        self.coins[coin_id] = new_pos

    def count_coins_in_pos(self, pos):
        count = 0
        for i in self.coins.keys():
            if pos == self.coins[i]:
                count += 1
        return count

