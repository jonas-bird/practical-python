#!/usr/bin/env python3
# pcost.py
# practical python workthrough
# typed out by: Jonas Bird
# Exercise 1.27, 1.30, 1.31, 1.32, 1.33

# import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    """ takes the filename of a csv file with an integer in the second column
and a double in the third, and returns the sum of the product of the two
columns in each row"""
    total_price = 0.0
    portfolio = read_portfolio(filename)
    for row in portfolio:
        total_price += row['price'] * row['shares']
    return total_price


def main(argv):
    if len(argv) == 2:
        csv_file = argv[1]
    else:
        csv_file = 'Data/portfolio.csv'

    cost = portfolio_cost(csv_file)
    print('Total cost: ', cost)


if __name__ == '__main__':
    main(sys.argv)
