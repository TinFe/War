from random import*
suits = ('clubs','diamonds','hearts','spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14 }

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:

            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) != type([]):
            self.all_cards.append(new_cards)
        else:
            self.all_cards.extend(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    

import time

war_list = []

def battle():
    print(f"{player0.name} draws the {player0cards[0]}")
    print(f"{player1.name} draws the {player1cards[0]}")
    if player0cards[-1].value > player1cards[-1].value:
        player0.add_cards(player0cards.pop(-1))
        player0.add_cards(player1cards.pop(-1))
        print(f'{player0.name} wins the battle!')

    elif player0cards[-1].value < player1cards[-1].value:
        player1.add_cards(player1cards.pop(-1))
        player1.add_cards(player0cards.pop(-1))
        print(f'{player1.name} wins the battle!')


def war():
    print("WAR!")

    
    print(f"{player0.name} drew the {player0cards[-1]}!")
    print(f"{player1.name} drew the {player1cards[-1]}!")
    
    if len(player0.all_cards) > 3:
        for i in range(4):
            player0cards.append(player0.remove_one())
    else:
        for i in range(len(player0.all_cards)):
            player0cards.append(player0.remove_one())
    
    if len(player1.all_cards) > 3:
        for i in range(4):
            player1cards.append(player1.remove_one())
    else:
        for i in range(len(player1.all_cards)):
            player1cards.append(player1.remove_one())
    
    if player0cards[-1].value > player1cards[-1].value:
        print(f'{player0.name} draws a {player0cards[-1]}')
        print(f'{player1.name} draws a {player1cards[-1]}') 
        print(f'{player0.name} wins the war!')
        player0.add_cards(player0cards)
        player0.add_cards(player1cards)
        player0cards.clear()
        player1cards.clear()
    elif player0cards[-1].value < player1cards[-1].value:
        print(f'{player0.name} draws a {player0cards[-1]}')
        print(f'{player1.name} draws a {player1cards[-1]}') 
        print(f'{player1.name} wins the war!')
        player1.add_cards(player1cards)
        player1.add_cards(player0cards)
        player0cards.clear()
        player1cards.clear()
    elif player0cards[-1].value == player1cards[-1].value:
        war()

    


player0 = Player("China")
player1 = Player('North Korea')
deck = Deck()
deck.shuffle_deck()
player0cards = []
player1cards = []

while len(deck.all_cards) > 0:
    player0.add_cards(deck.deal_one())
    player1.add_cards(deck.deal_one())



print(f"----{player0.name}'s cards----")
for i in range(len(player0.all_cards)):
    print(player0.all_cards[i])
print(f"----{player1.name}'s cards----")
for i in range(len(player1.all_cards)):
    print(player1.all_cards[i]) 


while True:

    if len(player0.all_cards) == 0:
        print(f'{player1.name} wins!')

        break
    elif len(player1.all_cards) == 0:
        print(f'{player0.name} wins!')
        break
    
    else:
        player0cards.append(player0.remove_one())
        player1cards.append(player1.remove_one())
        
        if player0cards[0].value != player1cards[0].value:
            battle()
            player0cards.clear()
            player1cards.clear()
            


        else:
            war()
            player0cards.clear()
            player1cards.clear()





