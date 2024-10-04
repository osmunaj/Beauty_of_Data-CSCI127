#RECURSION LAWS:
# 1. A recursive algorithm must have a base case
# 2. A recursive algorithm must change its state and move forward to the base case
# 3. A recursion algorithm must call itself inside of the function

# 1 2 3 4 5

from xml.etree.ElementPath import find


def findSum(numbers):
    if len(numbers) == 1:
        return numbers[0] #BASE CASE
    else:    # Changing the state        (Moving forward in the function)
        return numbers[0]+findSum(numbers[1:]) 

def findFactorial(n):
    if n == 0:
        return 1
    else:
        return n*findFactorial(n-1)
        
def fibinacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fibinacci(n-1)+fibinacci(n-2)

def sumDigits(n):
    if n==0: 
        return 0 
    else:
        return n%10 + sumDigits(int(n/10))

def power(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number*power(number,exponent-1)

def reverseList(list1):
    if(len(list1)==2):
        return []
    else:
        return reverseList(list1[1:]+list1[0])

def convert(base_10_number, new_base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base_10_number < new_base:
        return convert_string[base_10_number]
    else:
        return convert(base_10_number // new_base, new_base) + convert_string[base_10_number % new_base]
def unconvert(number, base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def parity(n):
    if n== 0 or n == 1:
        return n
    return parity(n-2)
    

def main():
    #print(findSum([1,2,3,4,5]))
    #print(findFactorial(4))
    #print(fibinacci(7))
    #print(sumDigits(452))
    #print(power(2,2))
    #print(reverseList([0,1,2,3,4,5]))

    print(parity(4 ))

    #print(convert(200, 11))
    #print(convert(100, 2))
    #print(convert(100, 36))
    # print(unconvert("100", 10))
    # print(unconvert("1100100", 2))
    # print(unconvert("2S", 36))
main()
