# report.py
#
# Exercise 2.4

import csv
import sys


def read_portfolio(filename):
    """recieves a filename for a csv file and returns list"""
    stock_portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            if len(row[0]) > 0:
                holding[headers[0]] = row[0]
                holding[headers[1]] = int(row[1])
                holding[headers[2]] = float(row[2])
                stock_portfolio.append(holding)
                continue
            next(rows)
    return stock_portfolio


if __name__ == '__main__':
    if len(sys.argv) == 2:
        csv_file = sys.argv[1]
    else:
        csv_file = 'Data/portfolio.csv'

stocks = read_portfolio(csv_file)
print(stocks)
