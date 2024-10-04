class Person:
    def __init__(self, name, age, hairColor):
        self.name = name
        self.age = age
        self.hairColor = hairColor

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getHairColor(self):
        return self.hairColor

    def birthDay(self):
        self.age += 1
        print("")

def main():
    ari = Person("Ari", 19, "Light Brown")
    print(ari.getAge)
    ari.birthDay
    print(ari.age)

main()
