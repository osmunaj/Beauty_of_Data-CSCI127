# -----------------------------------------+
# Ari Osmun                                |
# CSCI 127, Lab 3                          |
# Last Updated: (mm/dd/yyyy)               |
# Name:                                    |
# -----------------------------------------|
# Random letter from string                |
# -----------------------------------------+

# TODO: Write the print_random_letter function

import string
import random


def main(): 
    menu = '''
Thank you for running Lab Assignment 3
Please read carefully as our menu options may have changed:

Please press:
'E' - to enter a different string of text
'R' - to randomly choose a letter from the text
'M' - to repeat this menu again
'Q' - to quit this program

Current string:
012345....10...15...20...25...30...
↓↓↓↓↓↓↓↓↓↓↓    ↓    ↓    ↓    ↓'''
    current_string = "The quick red fox jumps over the lazy brown dog."
    
    print(menu)
    print(current_string)
    print()
    over = False
    while(not over):
        x = input("Enter your choice: ").upper()
        while (x != 'E') and (x != 'R') and (x != 'M') and (x != 'Q'):
            x = input("You must enter E, C, R, or Q: ").upper()
        if x == 'E':
            current_string = input("Enter the new string: ")
            print("Current string set to: ", current_string)
        elif x == 'R':
            print_random_letter(current_string)
        elif x == 'M':
            print(menu)
            print(current_string)
            print()
        else:
            over = True
            print("Goodbye.")

def print_random_letter(current_string):
    pass
    temp = ""
    for i in string:
        if(i.isalpha()):
            temp+=i
    if(len(temp)==0):
        print("Error: The current string has no letters in it.")
    else:
        index = random.randint(0,len(temp)-1)
        print(temp[index])

        
main()


