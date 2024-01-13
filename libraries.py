#Working with Libraries

from random import randint
from random import choice

""" class Die():

    def __init__(self, sides):
        self.sides = sides


    def roll(self):
        print(randint(1, self.sides))

dice = Die(6)
dice.roll()

dice2 = Die(10)
dice2.roll() """

class Lottery():

    def __init__(self):
        self.lottolist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

    def generate(self):
        print(choice(self.lottolist), choice(self.lottolist), choice(self.lottolist), choice(self.lottolist))

super15 = Lottery()
super15.generate()