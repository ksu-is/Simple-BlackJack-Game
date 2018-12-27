# need to add ace score either 11 or 1

from os import system
from colorama import Fore
from time import sleep
import random

'''Card class creates cards from self.deck[] list when called via deal_a_card()
method from the deck class. This creates a deck of cards each with attributes
of suit, rank & score. Method of display_card() from this class prints out the
card in form of colored ascii symbol and rank'''


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


'''Deck class is passed a list 'deck' becoming deck its single attribute.
Its methods include:
count() - Returns the number of list items(cards) in the deckself.
show_deck() - Prints every card in the deck using the Card class diplay_card.
new_deck() - Generates new 52 card deck iterating over each suit & rank combo.
shuffle_deck() - Randomises any new_deck() which is created in order.
deal_a_card() - Removes last list entry and returns a generated card.'''


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


'''Hand class needs to be passed 2x Card class instances & 'Player' or 'Dealer'
to generate card_list & player attributes. Methods include:
get_score() - Returns total score of the hand.
show_hand() - Displays Player/Dealer and their hand. Masks dealers 2nd card if
              True is passed, therefore on the dealers turn False needs to be
              passed to show the full hand.
hit() - Adds another card from the deck into the card_list attribute.
bust_check() - Uses the get_score() method to generate bust message and return
               True if over 21, returns False if not.
bj_check() - Checks if hand has initial blackjack/21 with 2 cards generating
             a message if so and returning True. If not False is returned.'''


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

    def bj_check(self):
        if self.get_score() == 21 and len(self.card_list) == 2:

            print('\nBLACKJACK!!!')
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
    if plyr_hand.bj_check() is True:
        return True
    while plyr_hand.get_score() < 22:
        turn = input('\nHit(h) or Stick(s)? ')
        if turn.lower() == 'h':
            plyr_hand.hit()
            game_state(False, True)
        elif turn.lower() == 's':
            return False


def dealer_turn():
    game_state(False, False)
    sleep(1)
    if dealer_hand.bj_check() is True:
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


def wincheck(pot, blackjack):
    if plyr_hand.get_score() > 21:
        winner = 'Dealer'
        pot -= float(bet)
    elif blackjack is True:
        winner = 'Player'
        pot += float(bet) * 1.5
    elif dealer_hand.get_score() > 21:
        winner = 'Player'
        pot += float(bet)
    elif dealer_hand.get_score() > plyr_hand.get_score():
        winner = 'Dealer'
        pot -= float(bet)
    elif dealer_hand.get_score() < plyr_hand.get_score():
        winner = 'Player'
        pot += float(bet)
    else:
        winner = 'Draw'
        print('Player and Dealer Draw This Hand.')

    if winner != 'Draw':
        print('\n{} Wins This Hand.'.format(winner))
    return pot


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
pot = 100.00

while game_flag is True:

    valid_bet = False
    message = ''
    bet = 0.00
    plyr_bj_check = False

    while valid_bet is False:

        if card_deck.count() < 10:
            card_deck.new_deck()
            card_deck.shuffle_deck()

        system('clear')
        print(f'Cash Pot is £{pot:.2f} {message}')
        bet = input('Please Place Your Bet: ')

        if bet.isalpha() is True:
            message = 'Last Bet Was Invalid.'
        elif float(bet) > pot:
            message = 'Last Bet Was Too High.'
        else:
            bet = float(bet)
            valid_bet = True

        # deal initial 2 card hands
    plyr_hand = (Hand([card_deck.deal_a_card(), card_deck.deal_a_card()],
                      'Player'))
    dealer_hand = (Hand([card_deck.deal_a_card(), card_deck.deal_a_card()],
                        'Dealer'))

    blackjack = plyr_turn()

    # player bust on turn
    if plyr_hand.get_score() > 21 or blackjack is True:
        pass

    else:
        dealer_turn()

    # end game routine
    pot = wincheck(pot, blackjack)
    another_game = input('\nPlay Another (y/n)? ')
    if another_game.lower() == 'n':
        game_flag = False
    elif pot <= 0.00:
        print('\nSorry You Have Gambled Away All Of Your Pot!!!')
        print('Game Over.')
        game_flag = False
    else:
        continue
