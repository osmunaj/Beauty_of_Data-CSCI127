
def list_sectors(file):
    print("GICS Sectors in the S&P 500".center(60, '-'))
    sp500 = open(file, 'r', errors="ignore")
    sp500 = readline()
    sectors = []
    num = 1
    for line in sp500:
        listing = line.split(',')
        if(listing[2] not in sectors):
            sectors.append(listing[2])
    sp500.close()
    sectors.sort()
    for sector in sectors:
        print(str(num) + '. ' + sector)
        num +=1
    print(''.center(60, '-'))
    return sectors

def get_user_choice(sectors):
    pass

def get_securities_in_sector(file, sector):
    pass

def generate_report(securities, sector):
    pass

def main(file):
    sectors = list_sectors(file)
    sector = get_user_choice(sectors)
    securities = get_securities_in_sector(file, sector)
    generate_report(securities, sector)

main("sp500.csv")


