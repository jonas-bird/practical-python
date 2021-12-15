#!usr/bin/env python3
# pcost.py
#
# Exercise 1.27

total_price = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')
        total_price += int(row[1]) * float(row[2])

print('Total cost ', total_price)
