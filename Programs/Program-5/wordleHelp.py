
def addToList(hint, falseLettersString, line):
    for i in range(5):
        condition1 = line[i] in falseLettersString
        condition2 = hint[i].isupper() and line[i] != hint[i].lower()
        condition3 = hint[i].islower() and hint[i] != " " and hint[i] not in line
        if(condition1 or condition2 or condition3):
            return False
        
    return True
    

def main(file):
    file = open(file)
    falseLetterString = ""
    falseLettersString = input("Type all letters which you know are not in the word")
    falseLetters = list(falseLettersString)
    hint = input("Input previous hint")
    if(len(hint)<5):
        hint += " "*(5-(len(hint)))
    for line in file:
        if addToList(hint, falseLettersString, line):
         print(line)
                
if __name__ == "__main__":
    main("knuth5letterwords.csv")
