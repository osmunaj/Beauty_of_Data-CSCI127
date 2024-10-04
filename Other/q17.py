def count_games(data):
    index = {}
    for line in data:
        games = line.split(",")
        index[games[0]] = len(games) - 1
    return index
def main():
    file = open("data.csv", "r")
    print(count_games(file))
    file.close()
main()
