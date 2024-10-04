# -----------------------------------------+
# Ari Osmun                                |
# CSCI 127, Program 2                      |
# Last Updated: (10/4/2022)                |
# Name: Ari Osmun                          |
# -----------------------------------------|
# Poker Hand Evaluation                    |
# -----------------------------------------+

# HINTS TO GET YOU STARTED:
# We use a list with two elements to model a card, and a list of five cards models a hand. 
# Data from a card [rank, suit], in a hand [card, card, card, card, card]
#   can be retrived like this: hand[2][1] (that example gives us the third card's suit).
# You can delete this function and its calls below once you understand it.
from re import A


def hint(hand):
    if (hand[0][0] == hand[1][0]):
        #return True # instead of returning the boolean value True, print message:
        print("Example: The first two cards both have the same rank. It is", hand[0][0])
    else:
        #return False # instead of returning the boolean value False, print message:
        print("Example: The first two cards do not have the same rank.")
print("Example Hints:")
hint([[2, "♠"], [7, "♣"], [4, "♦"], [8, "♦"], [6, "♥"]]) # no: first two ranks don't match
hint([[7, "♠"], [7, "♣"], [4, "♦"], [8, "♦"], [6, "♥"]]) # yes: first two ranks are both 7
print() # print a blank line

# Helper Function
# Given a poker hand as a list, return a list of the ranks
def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

# TODO:
# decide on parameters for the hand evaluation functions, and
# define functions to return True if the criteria is met; false otherwise
# you may more helper functions like the one above if you would like 

def five_of_a_kind(hand):
    # Check whether hand this hand contains JOKER card, and other cards all of the same suit.
    # change this expression. (This function as it is will always return False)
    return (hand[0][1]=="?" and (hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]))
    
def straight_flush(hand):
    if straight(hand):
        if(hand[0][1]=="?"):
            return(hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1])
        else:
            return (hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1])
    return False

def straight(hand):
    if(hand[0][0]==2 and hand[1][0]==3 and hand[2][0]==4 and hand[3][0]==5 and hand[4][0]==14): return True
    if(hand[0][1]=="?"):
        gaps = 0
        for i in range(2,5):
            if(int(hand[i][0])-(i-1)!=int(hand[1][0])):
                gaps +=1
                print("Gap at index ", i-1)
        
        return (gaps <= 1)
    return(int(hand[0][0])==(int(hand[1][0])-1)==(int(hand[2][0])-2)==(int(hand[3][0])-3)==(int(hand[4][0])-4))

def four_of_a_kind(hand):
    if(hand[0][1]=="?"):
        return (hand[1][0]==hand[2][0]==hand[3][0]) or (hand[2][0] == hand[3][0]==hand[4][0])
    else:
         return (hand [0][0] == hand[1][0] == hand[2][0] == hand[3][0]) or (hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0])
 
def full_house(hand):
    return ((hand[0][0]==hand[1][0]==hand[2][0]) and (hand[3][0]==hand[4][0])) or ((hand[0][0]==hand[1][0])and(hand[2][0]==hand[3][0]==hand[4][0]))

def flush(hand):
    return hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]

def three_of_a_kind(hand):
    return (hand[0][0]==hand[1][0]==hand[2][0])or(hand[1][0]==hand[2][0]==hand[3][0])or(hand[2][0]==hand[3][0]==hand[4][0])

def two_pair(hand):
    pairs = 0
    for i in range(-1,4):
        if(hand[i][0]==hand[i+1][0]):
            pairs+=1
    return (pairs == 2)

def pair(hand):
    for i in range(-1,4):
        if(hand[i][0]==hand[i+1][0]):
            return True


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    # Notice that once a hand is identified, no further evaluations are tried
    # Ex. A four of a kind is also a three of a kind, but evalutes to four of a kind
    poker_hand.sort() 
    print(poker_hand, "Poker Hand: ", end="")
    if five_of_a_kind(poker_hand):
        print("Five of a Kind")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand):
        print("Four of a Kind")
    elif full_house(poker_hand):
        print("Full House")
    elif flush(poker_hand):
        print("Flush")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand):
        print("Three of a Kind")
    elif two_pair(poker_hand):
        print("Two Pair")
    elif pair(poker_hand):
        print("One Pair")
    else:
        print("Nothing") # Can only beat another hand with nothing. (High card wins)
		
# -----------------------------------------+

def main():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14 # Ace always ranks highest
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    # The inline comments show how the card should be evaluted by the functions you write
    # The hands below are shown in order from worst to best. (ie: flush beats straight) 
    evaluate([[2, "♠"], [7, "♣"], [8, "♦"], [A, "♦"], [Q, "♥"]])    # High card
    print("-High card")
    evaluate([[T, "♠"], [Q, "♣"], [6, "♦"], [9, "♦"], [Q, "♥"]])    # One pair
    print("-One Pair")
    evaluate([[T, "♠"], [9, "♣"], [6, "♦"], [9, "♦"], [6, "♥"]])    # Two pair
    print("-Two Pair")
    evaluate([[K, "♦"], [7, "♣"], [7, "♥"], [8, "♣"], [7, "♠"]])    # Three of a kind
    print("-Three of a kind")
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♠"]])    # Straight
    print("-straight")
    evaluate([[2, "♥"], [9, "♥"], [3, "♥"], [6, "♥"], [T, "♥"]])    # Flush
    print("-Flush")
    evaluate([[8, "♦"], [7, "♣"], [8, "♥"], [8, "♣"], [7, "♠"]])    # Full house
    print("-Full house")
    evaluate([[2, "♦"], [7, "♣"], [2, "♥"], [2, "♣"], [2, "♠"]])    # Four of a kind
    print("-Four of a kind")
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♣"]])    # Straight flush   
    print("-Straight Flush") 
    evaluate([[7, "♥"], [0, "?"], [7, "♦"], [7, "♣"], [7, "♠"]])    # 5 of a kind ([0, "?"] is the Joker)
    print("-Five of a Kind")
    print("---------------------------------------")   
    print("Honor's Section Challenge:")
    evaluate([[3, "♣"], [4, "♣"], [2, "♣"], [A, "♣"], [5, "♠"]])    # stright (with low ace)
    print("-Straight, with low ace")
    evaluate([[2, "♥"], [0, "?"], [3, "♣"], [4, "♥"], [7, "♦"]])    # stright (with joker)
    print("-Straight, with joker")

# -----------------------------------------+

main()
