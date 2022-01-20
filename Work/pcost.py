#!/usr/bin/env python3
# pcost.py
# practical python workthrough
# typed out by: Jonas Bird
# Exercise 1.27, 1.30, 1.31, 1.32, 1.33

import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    """ takes the filename of a csv file with an integer in the second column
and a double in the third, and returns the sum of the product of the two
columns in each row"""
    total_price = 0.0
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for rowno, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             total_price += nshares * price
    #         # This catches errors in int() and float() conversions above
    #         except ValueError:
    #             print(f'Row {rowno}: Bad row: {row}')
    #             continue
    portfolio = read_portfolio(filename)
    for row in portfolio:
        total_price += row['price'] * row['shares']
    return total_price


if __name__ == '__main__':
    if len(sys.argv) == 2:
        csv_file = sys.argv[1]
    else:
        csv_file = 'Data/portfolio.csv'

    cost = portfolio_cost(csv_file)
    print('Total cost: ', cost)
