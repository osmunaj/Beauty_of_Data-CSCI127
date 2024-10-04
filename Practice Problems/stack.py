class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, num):
        self.items.append(num)

    def __iadd__(self, other):
        self.items.append(other)



def main():
    stack1 = Queue()
    
    for number in range(1, 6):
        stack1 += number


main()

