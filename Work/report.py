# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    """recieves a filename for a csv file and returns list"""
    stock_portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            stock_portfolio.append(holding)

    return stock_portfolio


if __name__ == '__main__':
    if len(sys.argv) == 2:
        csv_file = sys.argv[1]
    else:
        csv_file = 'Data/portfolio.csv'

    cost = portfolio_cost(csv_file)
    print('Total cost: ', cost)
