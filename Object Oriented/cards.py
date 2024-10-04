import card

class Deck:

    def __init__(self):
        self.cards = []
        for rank in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']:
            for suit in ['diamonds', 'hearts','clubs','spades']:
                self.cards += [Card(suit, rank)]

    def printDeck(self):
        print("52 Deck of Cards\n")

        number = 1
        for card in self.cards:
            print(str(number) + ") " + str(card))
            number += 1

        print()



def main():
    myDeck = Deck()
    myDeck.printDeck()
    print("Test card constructor")
    myCard = Card('seven','clubs')

main()


        
