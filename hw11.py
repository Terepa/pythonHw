# 1. The Shuffle

import itertools
import random


def get_shuffled_cards():
    suit = "diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"
    card = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"
    card_list = list(itertools.product(suit, card))
    random.shuffle(card_list)
    return card_list



# 2. Deck



class Deck:

    def __init__(self, card_list="", spent=""):
        suit = "diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"
        value = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"
        self.spent = spent
        self.card_list = (list(itertools.product(suit, value)))

    def shuffle(self):  # shuffle cards
        random.shuffle(self.card_list)
        return self

    def get_cards(self, count=1):
        if count > len(self.card_list):
            print("Cant get that much!")
        else:
            self.spent = self.card_list[:count]
            del self.card_list[0:count]
        return self.spent