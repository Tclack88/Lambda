#!/usr/bin/env python3

from random import randint, uniform
from acme import Product, BoxingGlove

prod = Product('A Cool Toy')
print(prod.name,prod.price,prod.weight,prod.flammability,prod.identifier)

prod.stealability()
prod.explode()

glove = BoxingGlove('boxing glove')
print('\nBoxing Glove:')
glove.explode()
glove.punch()
