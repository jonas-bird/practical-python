#!usr/bin/env python3
# pcost1.30.py
#
# Exercise 1.30

import csv
import sys

def portfolio_cost(filename):
    """takes a csv file, discards the first row, and multiplies an integer
    second column by a float third column"""

    total_price = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        number_of_shares = 0
        price_per_share = 0.0
        for row in rows:
            try:
                number_of_shares = int(row[1])
                price_per_share = float(row[2])
            except ValueError:
                print("Couldn't parse", row)
            total_price += number_of_shares * price_per_share
    return(total_price)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost ', cost)
