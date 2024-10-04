from email import message
import string

string.ascii_uppercase

def encrypt(message, offset): # TODO
    alpha = string.ascii_uppercase
    message = message.upper()
    
    secret = ""
    for c in message:
        secret += alpha[(alpha.index(c)+offset)%26]
    return secret


def main():
    message = input("what is your message? ")
    offset = input("what is the offset? ")
    print(encrypt(message, offset))

main()
