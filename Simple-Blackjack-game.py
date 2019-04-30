import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

play_round = 0

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):  
        if self.rank == 'Ace':
            return '%s of %s: value 11 or 1' %(self.rank, self.suit)   
        else:
            return '%s of %s: value %s' %(self.rank, self.suit, values[self.rank])
    
    
class Deck():
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        allcards = '\n'
        for item in self.deck:
            allcards += item.__str__() + '\n'
        return allcards
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Player:
    
    def __init__(self,total = 100):         
        self.total = total
        self.cards = []
        self.value = 0  
        self.aces = 0         
        self.bet = 0
    
    def add_card(self, card, values):
        self.cards.append(card)        
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

def total_budget(play_round, total):
    
    while True:    
        try:
            if play_round == 0:
                total = int(input("\nWhat is your budget: "))  
                if total <= 0:
                    print("Sorry. Budget can't be negative or zero")
                else:
                    return total
            else: 
                print("Your budget is " + str(total)) 
                return total                                               
        except ValueError:
            print("Please enter an integer!")

def take_bet(player):
    
    while True:    
        try:
            bet = int(input("What is your bet: "))  
            if bet <= player.total and bet > 0:
                player.bet = bet
                break   
            elif bet == 0:
                print("Your bet can't be 0")
            elif bet <= 0:
                print("Your bet can't be negative")
            else:
                print("Your bet can't exceed your total budget of ", player.total)       
        except ValueError:
            print("Please enter an integer!")

def show_some(player,dealer):    
    print("\nPlayer's cards are:")
    for item in player.cards:
        print(item)  
    print("\nDealer's cards are:")
    print('Secret card: value ?\n' + str(dealer.cards[1]))

def show_all(player,dealer):    
    print("\nPlayer's cards were:")
    for item in player.cards:
        print(item)        
    print("{Player's Hand: " + str(player.value) + "}") 
       
    print("\nDealer's cards were:")
    for item in dealer.cards:
        print(item)    
    print("{Dealer's Hand: " + str(dealer.value) + "}")    
    
def hit(deck,player_or_dealer):    
    player_or_dealer.add_card(deck.deal(), values)   
#   possible bug 
#   if player_or_dealer == player and player.aces > 0:
    if player_or_dealer.aces > 1:
        player_or_dealer.adjust_for_ace()
        
def hit_or_stand(deck, player_or_dealer, player, dealer):       
    
    while True:   
        choice = input("\nWould you prefer to hit or stay? Choose either 'H' or 'S': ").upper()               
        
        if choice == 'H':            
            hit(deck, player_or_dealer)
            show_some(player,dealer)            
            if player.value >= 21:
                break  
