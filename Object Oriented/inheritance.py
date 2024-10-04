class Pet:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.is_sleeping = s

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def set_age(self, a):
        self.age = a

    def get_age(self):
        return self.age

    def set_is_sleeping(self, s):
        self.is_sleeping = s

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"

class Dog(Pet):
    def __init__(self, name, age, sleep, b):
        super.__init__(name, age, sleep)
        self.breed = b

    



def main():
    pass

main()