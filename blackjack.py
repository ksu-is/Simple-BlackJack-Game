''' need to add score system, player blackjack on initial hand and
ace score either 11 or 1'''

from os import system
from colorama import Fore
from time import sleep
import random


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        if rank == 'K' or rank == 'Q' or rank == 'J':
            self.score = 10
        elif rank == 'A':
            self.score = 11
        else:
            self.score = int(rank)

    def display_card(self):
        if self.suit == diamond or self.suit == heart:
            print(Fore.RED + self.suit + Fore.WHITE + self.rank)
        else:
            print(Fore.WHITE + self.suit + ' ' + Fore.WHITE + self.rank)


class Deck:

    def __init__(self, deck):

        self.deck = deck

    def count(self):
        return len(self.deck)

    def show_deck(self):
        for suit, rank in self.deck:
            c = Card(suit, rank)
            c.display_card()

    def new_deck(self):
        self.deck = []
        for suit in suit_list:
            for rank in rank_list:
                self.deck.append((suit, rank))

    def shuffle_deck(self):
        system('clear')
        print('New Deck in play - Dealer Shuffling......')
        sleep(2.5)
        random.shuffle(self.deck)

    def deal_a_card(self):
        sel_card = self.deck.pop()
        return Card(sel_card[0], sel_card[1])


class Hand:

    def __init__(self, card_list, player):

        self.card_list = card_list
        self.player = player

    def get_score(self):
        total = 0
        for card in self.card_list:
            total += card.score
        return total

    def show_hand(self, mask_dealer):
        print('\n{}s Hand:'.format(self.player))
        if mask_dealer is True:
            self.card_list[0].display_card()
            print('???')
        else:
            for i in range(0, len(self.card_list)):
                self.card_list[i].display_card()

    def hit(self):
        self.card_list.append(card_deck.deal_a_card())

    def bust_check(self):
        if self.get_score() > 21:
            print('{} is BUST'.format(self.player))
            return True
        else:
            return False


# print game state & check if bust - passing True hides 2nd card & total
def game_state(plyr_cond, dealer_cond):
    system('clear')
    dealer_hand.show_hand(dealer_cond)
    if dealer_cond is False:
        print('Total: ' + str(dealer_hand.get_score()))
    dealer_hand.bust_check()
    plyr_hand.show_hand(plyr_cond)
    plyr_hand.bust_check()
    print('Total: ' + str(plyr_hand.get_score()))


def plyr_turn():
    game_state(False, True)
    while plyr_hand.get_score() < 22:
        # game_state(False, True)
        turn = raw_input('\nHit(h) or Stick(s)? ')
        if turn.lower() == 'h':
            plyr_hand.hit()
            game_state(False, True)
        elif turn.lower() == 's':
            return


def dealer_turn():
    game_state(False, False)
    sleep(1)
    if dealer_hand.get_score() == 21:
        print('\nDealer BLACKJACK!!!')
        return

    while dealer_hand.get_score() < 33:
        if dealer_hand.get_score() < 17:
            dealer_hand.hit()
            game_state(False, False)
            sleep(1)
        else:
            game_state(False, False)
            sleep(1)
            return


def wincheck():
    if plyr_hand.get_score() > 21:
        winner = 'Dealer'
    elif dealer_hand.get_score() > 21:
        winner = 'Player'
    elif dealer_hand.get_score() > plyr_hand.get_score():
        winner = 'Dealer'
    elif dealer_hand.get_score() < plyr_hand.get_score():
        winner = 'Player'
    else:
        winner = 'Draw'
        print('Player and Dealer Draw This Hand.')

    if winner != 'Draw':
        print('\n{} Wins This Hand.'.format(winner))


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
card_deck = Deck([])
card_deck.new_deck()
card_deck.shuffle_deck()

game_flag = True

while game_flag is True:

    if card_deck.count() < 10:
        card_deck.new_deck()
        card_deck.shuffle_deck()

    else:
        # deal initial 2 card hands
        plyr_hand = Hand([card_deck.deal_a_card(), card_deck.deal_a_card()], 'Player')
        dealer_hand = Hand([card_deck.deal_a_card(), card_deck.deal_a_card()], 'Dealer')
        plyr_turn()

        # player bust on turn
        if plyr_hand.get_score() > 21:
            pass

        else:
            dealer_turn()

        # end game routine
        wincheck()
        another_game = raw_input('\nPlay Another (y/n)? ')
        if another_game.lower() == 'n':
            game_flag = False
        else:
            continue
