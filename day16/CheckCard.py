class CheckCard:
    def __init__(self):
        self.data = ""

    def get_data(self):
        return self.data

    def set_data(self, data):
        while not self.check_valid(data):
            data = input("Invalid data! Please, re-enter the data:")
        self.data = data

    @staticmethod
    def check_valid(data):
        num_blocks = data.split("-")
        if len(num_blocks) != 4:
            return False
        else:
            block_len = len(num_blocks[0])
            for i in num_blocks:
                if len(i) != block_len or not i.isdigit():
                    return False
            return True

    @staticmethod
    def compare(card1, card2):
        return card1.data == card2.data

    def display(self):
        print("Card data:")
        print(self.data)


card = CheckCard()
card1 = CheckCard()
data = input("Please, enter card data:")
card.set_data(data)
card1.set_data(data)
print("Current data is: ", card.get_data())
card.display()
print("Cards are same? ", CheckCard.compare(card, card1))
