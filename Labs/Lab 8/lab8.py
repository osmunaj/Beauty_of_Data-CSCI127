# --------------------------------------
# CSCI 127, Lab 8                      |
# 10/18/2022                           |
# Ari Osmun                            |
# --------------------------------------

# The missing functions go here.

# Below are some hints for the first one to get you started.
# Familiarize yourself with the csv file by opening it in an editor first...

def create_dictionary(file): # f is the filename; rename the parameter as you wish

    # open the file for reading and assign to a file handle variable*
    readFile = open(file)
    # make a dictionary variable -- it can be empty to start with
    charDict = {}
    # use the file handle variable step through each line doing this...
    for line in readFile:
        # make the line into a list, splitting it up at the commas
        current = line.split(',')
        if (len(current) == 3):
            current[1] = ','
        current[1] = current[1].rstrip("\n")
        # optional: temporarily try printing it out. What you expected?
        #print(str(current))

        # assign the binary number to a variable as a string
        binaryNum = current[0]
        # optional: temporarily try printing it out. What you expected?
        # assign the character to a variable as a string
        character = current[1]
        if(character == "space"):
            character = " "
        if(character == "quote"):
            character = '"'
        if(character == "comma"):
            character == ','
        
        # optional: temporarily try printing it out. What you expected?
        # use the two new variables to add an entry to the dictionary
        charDict[character] = binaryNum
        # optional: temporarily try printing it out. What you expected?
        print(character + " | " + charDict[character])
    # optional: temporarily try printing the finished dictionary. What you expected?
    # Note: you will want the comma, space, and quote mark keys to be those actual characters...
    # ...make sure that gets handled at some point before returning the dictionary
    # *don't forget to close the file
    readFile.close()
    # return the dictionary to where it was called from
    return charDict

def translate(s, d, f): # rename the parameters as you wish
    output = ""
    for char in s:
        if char in d:
            output += d[char]
        else:
            output += "\nUNDEFINED\n"
    writeFile = open(f, 'w')
    writeFile.write(output)
    writeFile.close()


def decode(s, d): # rename the parameters as you wish
    pass

def verify(f1, f2):
    read1 = open(f1)
    read2 = open(f2)
    print(read1.read() == read2.read())
# --------------------------------------
def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")
    
    # Honors Section challange:
    decode('010001110110111101101111011001000010000001101010011011110110001000100001', dictionary)


# --------------------------------------

main()
