#!/usr/bin/env python3

from random import randint, uniform

class Product:
    def __init__(self,name=None, price=10, weight = 20,
            flammability=.5, identifier=uniform(1000000,10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        price_weight_ratio = self.price/self.weight
        if price_weight_ratio < .5:
            stealability_desc = 'Not so stealable...'
            print(stealability_desc)
            return(stealability_desc)
        elif price_weight_ratio < 1:
            stealability_desc = 'Kinda stealable.'
            print(stealability_desc)
            return(stealability_desc)

        else:
            stealability_desc = 'very stealable!'
            print(stealability_desc)
            return(stealability_desc)


    def explode(self):
        explosion_factor = self.flammability * self.weight
        if explosion_factor < 10:
            print("...fizzle")
            return "...fizzle" 
        elif explosion_factor < 50:
            print("...boom!")
            return "...boom!"
        else:
            print("...BABOOM! !")
            return "...BABOOM! !"


class BoxingGlove(Product):
    def __init__(self,name=None, price=10, weight=10,
            flammability=.5, identifier=uniform(1000000,10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


    def explode(self):
        print("...it's a glove")

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif self.weight < 15:
            print('Hey that hurt!')

        else:
            print('OUTCH!!')



