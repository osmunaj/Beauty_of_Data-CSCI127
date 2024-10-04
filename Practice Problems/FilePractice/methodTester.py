def main():

    #fileHandle = open("testFile.txt", "r")

    #aline = fileHandle.readline()
    #print(aline)

    
    #lineList = fileHandle.readlines()
    #print(lineList)

    #fileHandle = open("testFIle.txt", "r")
    #fileString = fileHandle.read()
    #print("FILESTRING IS", fileString)
    fileHandle = open("data/census2020.csv", "r")
    fileHandle.readline()
    for line in fileHandle:
        items = line.split(",")
        print(items)
main()
