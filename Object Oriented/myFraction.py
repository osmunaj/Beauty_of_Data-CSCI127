import math

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
    
    def __eq__(self, other):
        return (self.getNum() * other.getDen() == self.getDen() * other.getNum())
    
    def simplify(self):
        common = gcd(self.getNum(), self.den())


    

def main():
    fraction1 = Fraction(5,6)
    fraction2 = Fraction(1,2)
    fraction3 = Fraction(4, 8)
    print(fraction1)
    fraction1.num = 7
    print(fraction1)
    print(fraction2)
    print(fraction1 == fraction3)


    

main()