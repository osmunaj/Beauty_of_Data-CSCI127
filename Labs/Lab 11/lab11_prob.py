import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# Month __, 20__
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die with given number of sides"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Farkle:

    def __init__(self, sides):
        """A constructor method that can record 6 dice rolls"""
        self.rolls = np.zeros(6, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 6 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
        
#--------------------------------------------------

    def is_it_four_of_a_kind(self):
        return 4 in self.count_outcomes()[1:]
        '''temp = self.count_outcomes()[1:]
        found = False
        for i in temp:
            if i == 4:
                found = True
        return found'''
    
    def is_it_straight(self):
        for i in self.count_outcomes()[1:]:
            if i != 1:
                return False
        return True
        '''temp = np.array(self.count_outcomes()[1:])
        score = np.count_nonzero(temp)
        if (score == 6):
            return True'''
        
    
    def is_it_two_triplets(self):
        count = 0
        for i in self.count_outcomes()[1:]:
            if i == 3:
                count += 1
        return count == 2

# -------------------------------------------------
        
def main(how_many):

    four_of_a_kind = 0
    straight = 0
    two_triplets = 0
    game = Farkle(6)

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_four_of_a_kind():
            four_of_a_kind += 1
        elif game.is_it_straight():
            straight += 1
        elif game.is_it_two_triplets():
            two_triplets += 1

    

    print("Number of Rolls:", how_many)
    print("---------------------")
    
    if four_of_a_kind == 0:
        print("No Four of a Kinds were rolled\n")
    else:
        print("Number of Four of a Kinds:", four_of_a_kind)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/four_of_a_kind))
    if straight == 0:
        print("No Straights were rolled\n")
    else: 
        print("Number of Straights:", straight)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/straight))
    if two_triplets == 0:
        print("No Two Triplets were rolled\n")
    else:
        print("Number of Two Triplets:", two_triplets)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/two_triplets))

# -------------------------------------------------

if __name__ == "__main__":
    main(10000)
    
        
