#!usr/bin/env python3
# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    """ takes the filename of a csv file with an integer in the second column
and a double in the third, and returns the sum of the product of the two
columns in each row"""
    total_price = 0.0
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            row = line.split(',')
            total_price += int(row[1]) * float(row[2])
    return total_price


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ', cost)
