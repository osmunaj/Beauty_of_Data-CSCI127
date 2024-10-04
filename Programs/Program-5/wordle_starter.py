import random

# -------------------------------------------------
# CSCI 127, Program 5: WORDLE
# November 27th, 2022
# Ari Osmun
# -------------------------------------------------
 
class Wordle:

    def __init__(self, letters_in_word, file_of_words):
        self.num_letters = letters_in_word
        self.word_list = open(file_of_words, 'r').read().upper().splitlines()
        self.answer = self.word_list[random.randint(0, len(self.word_list)-1)]
        self.cheat_code = "?"
        self.test_code = "!"
        self.turn_num = 0

    def change_answer(self, new_answer):
        self.answer = new_answer.upper()

    def get_player_guess(self):
        self.turn_num += 1
        user_word = input("Enter your guess: ").upper()
        if(user_word == self.cheat_code):
            self.turn_num -= 1
            print("\tPsst. Answer is", self.answer)
            user_word = self.get_player_guess()
        if(user_word == self.test_code):
            self.turn_num -= 1
            new_answer = input("\tOkay. Enter the new answer: ").upper()
            while new_answer not in self.word_list:
                new_answer = input("\tEnter a valid " + str(self.num_letters) + " letter word: ").upper()
            self.change_answer(new_answer)
            print("\tAnswer set to " + new_answer.upper())
            user_word = self.get_player_guess()
        while len(user_word) != self.num_letters or user_word not in self.word_list:
            if(len(user_word) != self.num_letters):
                user_word = input("Word must be " + str(self.num_letters) + " letters. Enter a valid input: ").upper()
            if (user_word not in self.word_list):
                user_word = input("That word is not in the list. Enter a valid input: ").upper()
        # TODO (20 pts): loop until player enters a word that has both the correct number of letters AND is a word in the word list

        return (user_word.upper())

    def generate_hint(self, guess):
        print('\n\t' + guess)
        hint = ""
        if(guess == self.answer):
            return guess # Game over!
        # TODO (50 pts): Write the game logic for WORDLE hints. Assume guess and answer will contain 5 unique letters (STEAL, BLAME, CROPS)
        #WRITTEN CODE 
        for i in range(5):
            if guess[i] == self.answer[i]:
                hint += guess[i]
            elif guess[i] in self.answer:
                hint += guess[i].lower()
            else:
                hint += '-'
        print(hint)
        
        # HONORS SECTION ONLY (10 pts): Support guesses and answers that use the same letter multiple times (STEEL, EVERY, POPPY)
        
        return(hint)

def main(file):

    game = Wordle(5, file)
    print("\nWelcome to WORDLE!\n")
    guess = ""
    
    while(guess != game.answer and game.turn_num < 6):
        print(game.turn_num+1, end='. ')
        guess = game.get_player_guess()
        print('\t'+ game.generate_hint(guess) + '\n')
        
    # TODO (15 pts): If the player gets the word on the first guess, print, "Wow! You're either very lucky, or you got some insider information."
    # If they get it on the sixth guess, print, "Phew! You got it on the last try!"
    # But if they take 2-5 guesses, print, "GREAT! You got it in <num> tries." (where <num> is the number of guesses it took.)

    # TODO: (15 points) If the player runs out of guesses (uses all six), print, "Game Over. Reveal answer? y/n: "
    # and if they enter y or Y, print, "Answer was <answer>." (where <answer> is the word they were trying to guess)
    # if they enter anything else, just print, "Thanks for playing."
    
    if game.turn_num == 1:
        print("Wow! You're either very lucky, or you got some insider information.")
    elif 1 < game.turn_num < 5:
        print("GREAT! You got it in " + str(game.turn_num) + " tries!")
    elif game.turn_num == 6:
        if(guess != game.answer):
            ans = input("Game Over. Reveal answer? y/n: ")
            if(ans.upper() == "Y"):
                print("Answer was " + game.answer + ".")
        else:
            print("Phew! You got it on the last try!")
    print("Thanks for playing.\n")
    
if __name__ == "__main__":
    main("knuth5letterwords.csv")
