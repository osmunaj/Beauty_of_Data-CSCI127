#Object oriented paradime

class Drink():
    """ Model a blended drink """ # docstring comment

    def __init__(self, ingredients, time):
        self.contents = ingredients
        self.duration = time
        self.result = 'not blended yet'

    def blend(self):
        if self.contents !=[] and self.duration > 0:
            self.result = (self.contents, "blended for", self.duration, "seconds")
        else:
            self.result = "problem with blending"        



def main():
    ingredients1 = ['berries', 'milk', 'ice']
    smoothie = Drink(ingredients1, 60)
    smoothie.blend()
    print(smoothie.result)


    ingredients2 = ['cookies', 'milk','ice cream']
    milkshake = Drink(ingredients2, 30)
    milkshake.blend()
    print(milkshake.result)

main()
    
