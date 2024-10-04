from functools import total_ordering
import random
import math
def main():
    calculatePi(10000000)

def calculatePi(samples):
    totalIns = 0
    totalOuts = 0
    for sample in range(samples):
        x = random.random()
        y = random.random()
        if(math.sqrt((x**2)+(y**2))>=1):
            totalOuts+=1
        else:
            totalIns+=1
    print((totalIns/sample)*4)

main()

