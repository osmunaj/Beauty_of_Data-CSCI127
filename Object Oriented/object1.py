class Cake:
    def __init__(self, food):
        self.food = food

    def bake(self, temp, time):
        print("Baking ", self.food, " at ", temp ' degrees for ',time, ' minutes')




ingredients = {'eggs' : 2, 'flour' : 'half a cup', 'sugar': 'tons'}

myCake = Cake(ingredients)
myCake.bake(440, 30)