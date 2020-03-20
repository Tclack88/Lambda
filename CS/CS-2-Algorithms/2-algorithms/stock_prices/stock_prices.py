#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = float("-inf") # start with neg. infinity (account for least worse loss)
    for p in range(1,len(prices)):
        profit = prices[p] - min(prices[:p])
        if profit > max_profit:
            max_profit = profit
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
