class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return "The " + str(self.rank) + " of " + str(self.suit)
