#!/usr/bin/env python3


import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, ITEMS
from random import randint

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        print("testing default price is 10")
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_price_generationi(self):
        """Test max price is no greater than 100"""
        print("testing price generation")
        prices = [Product('test').price for _ in range(100)]
        self.assertTrue(max(prices) <= 100)

    def test_stealability_words_present(self):
        """Test presence of all 3 possible stealability explanations
        (only ['Not so stealable...','Kinda stealable.','very stealable!'] allowed)"""
        print("testing stealability words...")
        possible_stealability_words = ['Not so stealable...',
                'Kinda stealable.','very stealable!']
        stealability_output = [Product("test",randint(1,100),randint(1,100)).stealability() for _ in range(100)]
        stealability_output = list(set(stealability_output)) # return only unique output
        for result in stealability_output:
            self.assertTrue(result in possible_stealability_words)

if __name__ == '__main__':
    unittest.main()
