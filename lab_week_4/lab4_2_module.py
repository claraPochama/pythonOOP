import random

class card: 
    def __init__(self, rank, suit): # rank of a suit
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank + " of " + self.suit

class deck: 
    def __init__(self): # rank of a suit
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(rank, suit))
    def shuffle(self): 
        #print("(shuffled)")
        random.shuffle(self.cards) 
    def deal(self): 
        #print("(a pop)")
        return self.cards.pop()
    def count(self): 
        return len(self.cards)