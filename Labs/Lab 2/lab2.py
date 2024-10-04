import random
import math


def main():
    a=random.randint(1,10)
    b=(random.random()*20)-10
    c=random.randint(-10,0)
    print("a=",a, "b=",b,"c=",c)
    print()
    print("0=",a,"x^2+",b,"x",c)
    print("(-",b,"+-(",b,"^2-4*",a,"*",c,")^(1/2))/(2*",a,")")
    print()
    print("x=",((-1*b)+math.sqrt((b*b)-(4*a*c)))/2*a)
    print("x=",((-1*b)-math.sqrt((b*b)-(4*a*c)))/2*a)

main()