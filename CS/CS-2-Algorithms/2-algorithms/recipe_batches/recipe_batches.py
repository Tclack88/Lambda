#!/usr/bin/python

from collections import Counter

def recipe_batches(recipe, ingredients):
    recipe_ingredients = set(recipe.keys())
    ingredients = Counter(ingredients)  # cannot subtract dictionaries so use
    recipe = Counter(recipe)            # Counter class instead

    batches = 0
    ingredients_remain = True
    while ingredients_remain:
        ingredients.subtract(recipe)    
        ingredients = Counter(dict(filter(lambda x: x[1] >= 0, ingredients.items())))
        # "-" automatically removes zero and negatives. We want to keep 0's because
        # it's a "perfect" match. Filter out negatives however
        if set(ingredients.keys()).intersection(recipe) == recipe_ingredients:
            # ignore superfluous "ingredients" not apart of recipe, if ingredients
            # remain after subtraction, a batch has been succesfully made
            batches += 1
        else:
            ingredients_remain = False
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
