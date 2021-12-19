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
        # should be name, shares, price
        portfolio_headers = next(rows)
        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(portfolio_headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                stock_portfolio.append(record)
                continue
            except ValueError:
                print(f'Row {row_num}: Bad data: {row}')
            next(rows)
    return stock_portfolio


def read_prices(filename):
    """reads a list of stock symbols and prices from a csv file and returns
    a dictionary with the stock symbol as key and the price as value"""
    stock_prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except:
                continue

    return stock_prices


def make_report(stock_list, prices_dict):
    """takes a list of dictionaries representing stock holdings and a
    dictionary of stock symbols and the current price and returns a list
    of tuples"""
    stock_status = []
    for stock in stock_list:
        stock_info = (
            stock['name'],
            int(stock['shares']),
            float(prices_dict[stock['name']]),
            float((prices_dict[stock['name']] - stock['price']))
        )
        stock_status.append(stock_info)
    return stock_status


if __name__ == '__main__':

    if len(sys.argv) == 3:
        holdings_file = sys.argv[1]
        prices_file = sys.argv[2]
    else:
        holdings_file = 'Data/portfolio.csv'
        prices_file = 'Data/prices.csv'

    stocks = read_portfolio(holdings_file)
    prices = read_prices(prices_file)
    stock_report = make_report(stocks, prices)

    # output the report generated in make_report
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in stock_report:
        print(f'{name:>10s} {shares:>10d} {"$" + str(price):>10s} {change:>10.2f}')
