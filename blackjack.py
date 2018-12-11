from colorama import Fore
import random


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        if rank == 'K' or rank == 'Q' or rank == 'J':
            self.score = 10
        elif rank == 'A':
            self.score = 1
        else:
            self.score = int(rank)

    def display_card(self):
        if self.suit == diamond or self.suit == heart:
            print(Fore.RED + self.suit + Fore.WHITE + self.rank)
        else:
            print(Fore.WHITE + self.suit + ' ' + Fore.WHITE + self.rank)


def new_deck():
    card_deck = []
    for suit in suit_list:
        for rank in rank_list:
            card_deck.append((suit, rank))
    return card_deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_a_card(card_deck):
    sel_card = card_deck.pop()
    return Card(sel_card[0], sel_card[1])


def get_score(hand):
    score = 0
    for card in hand:
        score += card.score
    return score


def show_game_state(plyr_hand, comp_hand):
    print('Computers Hand:')
    comp_hand[0].display_card()
    print('???')

    print('\nPlayers Hand:')
    for item in plyr_hand:
        item.display_card()
    print('Total: ' + str(get_score(plyr_hand)))


# assign suit symbols
club = u"\u2667"
spade = u"\u2664"
heart = u"\u2665"
diamond = u"\u2666"

# create lists of possible suits & ranks
suit_list = [heart, club, spade, diamond]
pic_cards = ['J', 'Q', 'K', 'A']
rank_list = [str(x) for x in range(2, 11)] + pic_cards

# create deck and shuffle
card_deck = new_deck()
card_deck = shuffle_deck(card_deck)

# create start hands for plyr & comp
plyr_hand = [deal_a_card(card_deck), deal_a_card(card_deck)]
comp_hand = [deal_a_card(card_deck), deal_a_card(card_deck)]

show_game_state(plyr_hand, comp_hand)
