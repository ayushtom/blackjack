import random as rd
playing = True

suits=('spades','diamonds','clubs','spades')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suit
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value=self.value+values[card.rank]
        
        if card.rank=='ace':
            self.aces=self.aces+1
        
    def adjust_ace(self):
        if self.value>21 and self.aces>0:
            self.value=self.value-10
            self.aces=self.aces-1
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits :
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp=deck_comp +'\n'+ card.__str__()
        return "the deck has: " + deck_comp
    
    def shuffle(self):
        rd.shuffle(self.deck)
    
    def deal(self):
        single_card=self.deck.pop()
        return single_card
class chip:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
        
    def win_bet(self):
        self.total=self.total+self.bet
        
    def lose_bet(self):
        self.total=self.total-self.bet
def place_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter the amount of bet placed"))
        except:
            print("Enter a valid integer")
            continue
        else:
            if chips.bet>chips.total:
                print("Not Enough Money")
            else:
                break   

def hit(hand,deck):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()

def hit_stand(hand,deck):
    global playing
    while True:
        print("\n")
        c=(input("Enter h for hit and s for Stand \n"))
        if c[0].lower()=='h':
            hit(hand,deck)
        elif c[0].lower()=='s':
            print("Player Stands Dealer's Turn")
            playing=False
            break
        else:
            print("Invalid choice")
            continue
        print("\n")
        break    

def player_busts(player,dealer,chips):
    print("\nPlayer Busts! \n")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("\nPlayer Wins! \n")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer  Busts! \n")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer Wins \n");
    chips.win_bet()
    
def push(player,dealer,chips):
    print("\nIt's a tie!PUSH \n")

def show_some(player,dealer):
    print("Player's hands")
    for card in player.cards:
        print(card)
    print("\n")
    print("dealer's hands")
    print("one card hidden!")
    print(dealer.cards[1])
    
def show_all(player,dealer):
    print("player's hands")
    for card in player.cards:
        print(card)
    print("\n")
    print("dealer's hands")
    for card in dealer.cards:
        print(card)


while (True):
    print("WELCOME TO BLACKJACK")
    
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips=chip()
    
    place_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing==True:
        
        hit_stand(player_hand,deck)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            show_all(player_hand,dealer_hand)
            break
            
        
    
    
    if player_hand.value<=21:
        
        while dealer_hand.value<=21:
            hit(dealer_hand,deck)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value>21:
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value>dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)
            
    print(" \n Player total chips are : {}".format(player_chips.total))
    
    
    new_game=input("enter 'y' to play again and 'n' to end the game")    
    if(new_game[0].lower()=='y'):
        playing=True
        continue
    else:
        print("thank you for playing!")
        break
        
            
