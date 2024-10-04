import math
import random

class Point:
    x:float
    y:float

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def magnitude(self):
        mag = math.sqrt((self.x**2) + (self.y**2))  
        return mag

def main():
    inside = 0
    for i in range(1000000):
        x = random.random()
        y = random.random()
        mag = Point(x, y).magnitude()
        if(mag <= 1):
            inside += 1
        if(i <= 4):
            print("\nSample " + str(i+1) + " is (" + str(x) + '", "' + str(y) + ")")
            print("Distance from origion of sample: " + str(mag)+ "\n")
    
    pi_estimate = 4*(inside/1000000)
    print("number of points insdie circle: " + str(inside) + "/1000000\n")
    print("pi estimate: \n" + str(pi_estimate))
    print("pi actual: \n" + str(math.pi))
    print("off by " + str(pi_estimate - math.pi))

main()
