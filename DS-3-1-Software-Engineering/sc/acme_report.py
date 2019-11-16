#!/usr/bin/env python3

from random import randint, uniform, choice
from acme import Product

ITEMS ="toothbrush toilet house twister eraser sharpie pants fake_flowers blanket thread beef television clay_pot twezzers book teddy piano washing_machine air_freshener desk nail computer bed sofa shampoo shoes cinder_block lamp_shade toothpaste floor" .split()

ADJECTIVES = "remarkable tall suspicious confident unfair substantial happy angry aggressive conscious guilty impossible sudden decent electrical available weak mad administrative relevant".split()

def generate_products(n=30):
    """ returns a list from two other lists (ADJECTIVES and ITEMS)
    to randomly generate products
    """
    products = []
    for i in range(n):
        adj = choice(ADJECTIVES)
        item = choice(ITEMS)
        name = f'{adj} {item}'
        product = Product(name,
                randint(5,101),
                randint(5,101),
                uniform(0,2.5),
                randint(100000,1000000))
        products.append(product)
    return products


def inventory_report(products):
    for product in products:
        print("\n\nName:\t",product.name)
        print("ID:\t",product.identifier)
        print("Weight:\t",product.weight)
        print("price:\t$",product.price)
        product.stealability()
        print("flammability:\t",product.flammability)
        product.explode()


if __name__ == '__main__':
    inventory_report(generate_products())


#After programming in python for nearly a year and a half, as of Friday November 1st 2019 10:14 am pacific, I finally understand what this if __name__ = __main__ business is all about!
