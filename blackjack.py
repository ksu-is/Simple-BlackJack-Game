from colorama import Fore
import random


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        if rank == 'King' or rank == 'Queen' or rank == 'Jack':
            self.score = 10
        elif rank == 'Ace':
            self.score = 1
        else:
            self.score = int(rank)

    def show_card(self):
        if str(rank).isalpha():
            print(Fore.WHITE + str(rank[0]), end='')
        else:
            print(Fore.WHITE + str(rank), end='')

        if suit == heart or suit == diamond:
            print(Fore.RED + suit)
        else:
            print(suit)


# generate deck of cards
club = u"\u2667"
spade = u"\u2664"
heart = u"\u2665"
diamond = u"\u2666"

suit_list = [heart, club, spade, diamond]
pic_cards = ['Jack', 'Queen', 'King', 'Ace']
rank_list = [x for x in range(2, 11)] + pic_cards

card_deck = []

for suit in suit_list:
    for rank in rank_list:
        card_deck.append((suit, rank))
        current = Card(suit, rank)
        current.show_card()
