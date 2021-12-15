#!usr/bin/env python3
# pcost.py
# practical python workthrough
# typed out by: Jonas Bird
# Exercise 1.27, 1.30, 1.31, 1.32

import csv

def portfolio_cost(filename):
    """ takes the filename of a csv file with an integer in the second column
and a double in the third, and returns the sum of the product of the two
columns in each row"""
    total_price = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                total_price += int(row[1]) * float(row[2])
            except:
                print('Bad data in row, skipping')
                continue
    return total_price


if __name__ == '__main__':
    cost = portfolio_cost('Data/portfolio.csv')
    print('Total cost: ', cost)
