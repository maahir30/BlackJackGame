import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
   
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp = deck_comp + "\n" + card.__str__()
        return 'Here is the deck:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # card is from Deck.deal() 
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        
        if card.rank == "Ace":
            self.aces = self.aces + 1
            
    
    def adjust_for_ace(self):
        
        #If the total value is greater than 21 for the players hand, and they have an ACE
        #It turns the ACE from an 11 to a 1
        while self.value > 21 and self.aces > 0:
            self.value = self.value - 10
            self.aces = self.aces -1
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet 
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please enter an integer for your bet: "))
        except:
            print("Looks like you did not enter an integer! Please try again.")
            continue
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet of ' + str(chips.bet) + ' is more than you have.')
                continue  
            else:
                print("Your bet of " + str(chips.bet) + " has been placed!")
                break
               
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

        
    while True :
        hit_stand = input("Do you want to hit or stand? Answer h or s.")
        if hit_stand[0].lower() == 'h':
            hit(deck,hand)
            print('You have hit.')
            break
        elif hit_stand[0].lower() == 's':
            print("Players stands, Dealer's turn")
            playing = False
            break
        else:
            print('I could not understand your statement. Please try again. Enter h or s only.')
            continue 
def show_some(player,dealer):
    print('\nDealers Cards:')
    print('>hidden card<')
    print('',dealer.cards[1])
    print('\nPlayers Cards: ',*player.cards, sep='\n ')
    
def show_all(player,dealer):
    print('\nDealers Cards: ',*dealer.cards,'\nTotal Dealer Value: ',dealer.value , sep='\n ')  
    print('\nPlayers Cards: ',*player.cards,'\nTotal Player Value: ',player.value , sep='\n ')
    
def player_busts(player,dealer,chips):
    chips.lose_bet()
    print("Player has BUST. You have lost the game along with your bet of " + str(chips.bet) + ".")
    print("\nYou now have " + str(chips.total) + " chips left.")
    
    

def player_wins(player,dealer,chips):
    chips.win_bet()
    print("Player has WON. You have won your bet of " + str(chips.bet) + ".")
    print("\nYou now have " + str(chips.total) + " chips in total.")
    

def dealer_busts(player,dealer,chips):
    chips.win_bet()
    print("Dealer has BUST. You won the game along with your bet of " + str(chips.bet) + ".")
    print("\nYou now have " + str(chips.total) + " chips in total.")


def dealer_wins(player,dealer,chips):
    chips.lose_bet()
    print("Dealer has WON. You have lost the game along with your bet of " + str(chips.bet) + ".")
    print("\nYou now have " + str(chips.total) + " chips left.")
    
    
def push(player,dealer,chips):
    print('Player and Dealer have tied. PUSH') 

game_on = True
print('Welcome to BlackJack!')
while game_on:

    
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    
    player_hand = Hand()
    player_hand.add_card(deck.deal()) 
    player_hand.add_card(deck.deal()) 
    
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    # Set up the Player's chips
    player_chips = Chips()
    print('You currently have ' + str(self.total) + ' chips in total.'
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
        else:
            continue

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while True:
            if dealer_hand.value < 17:
                hit(deck,dealer_hand)
                continue
            else:
                break
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif player_hand.value == dealer_hand.value:
            push(player_hand,dealer_hand,player_chips)
    
    # Inform Player of their chips total 
    
    # Ask to play again     
    while True :
        play_again = input('Do you want to play again? Answer y or n.')
        if play_again[0].lower() == 'y':
            game_on = True
            break
        elif play_again[0].lower() == 'n':
            print("GAME OVER")
            game_on = False
            break
        else:
            print('I could not understand your statement. Please try again. Enter y or n only.')
            continue 
