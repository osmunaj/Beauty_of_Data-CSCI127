def main():
    file = open("AEHousman.txt", "r")
    totalChars = 0
    totalLines = 0
    for line in file:
        totalLines += 1
        totalChars += len(line)
    average = round(totalChars/totalLines, 2)
    print("Average Number of characters per line: " + str(average))
main()
