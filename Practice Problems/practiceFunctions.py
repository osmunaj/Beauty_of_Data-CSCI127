from random import randint
import string


def getYear():
    age = int(input("How old are you?"))
    birthYear = (2022-age)
    return birthYear

def strings():
    #       012345678910
    word = "hello world"
    print(word[0])            #index 0
    print(word[0:6])          #index 0 to 6, does not include index 6
    print(word[6:])           # index 6 to the end
    print(len(word))          #length of word
    print(word.upper())       #returns uppercase word | ALSO .upper is a method, not a function
    print(word.find('world')) #Finds index 
    print(word.count('l'))    #Counts number of l's
    print(string.ascii_uppercase)
    print(string.ascii_lowercase)
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)
    print(string.__all__)

def forExample():
    for i in range (10): #Run 10 times starting at 0
        print("Run: ",i)
    
def fruityFunction(times): #Times is a parameter
    for i in range(times):
        print("Times is a parameter")
    return ("a fruitful function returns something")

def rollADice(sides):
    return randint(1,sides) 

def getTime():
    day = input("What's today? ")
    time = float(input("what time is it"))

def emptyStatement():
    pass #Pass fills the function without 

def alternate_case (sentence, start = 0):
    result = ""
    upper = True
    for i in range(len(sentence)):
        if i < start:
            result = result + sentence[i]
        elif upper:
            result = result + sentence[i].upper()
        else:
            result = result + sentence[i].lower()
        upper = not upper
    return result

def iteration():
    word = "hello"
    for i in word:
        print(i)
    print()
    x=0
    while (x != 5):
        print(x)
        x+=1
    colors = "red","orange","yellow","green","blue","purple"
    for color in colors:
        print("color is",color)
    userSays = "yes"
    while(userSays != "no"):
        userSays = input("Keep playing? ")
        userSays="no"
    for row in range(1,13):
        print()
        for colum in range(1,13):
            print(row*colum, end="\t")

def question10(int1, str1):
    return (len(str1)>int1) 

def question11():
    length = int(input("How many letters in the password?"))
    letters = string.ascii_uppercase
    temp = ""
    for i in range(length):
        temp += letters[randint(0,len(letters)-1)]
    print(temp)

def main():
    #print(getYear())
    #forExample()
    #print(fruityFunction())
    #print (rollADice(4))
    #strings()
    #iteration()
    # print(question10(3, "word"))
    # print(question10(4, "word"))
    # print(question10(6, "goose"))
    question11()

main()
