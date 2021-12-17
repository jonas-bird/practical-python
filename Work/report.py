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
        stock_info = {
            'name': stock['name'],
            'shares': stock['shares'],
            'price': prices_dict[stock['name']],
            'change': (prices_dict[stock['name']] - stock['price'])
        }
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

    #  stocks_change = {}
    # total_value = 0.0
    # old_value = 0.0

#    for stock in stocks:

       #  total_value += (stock['shares'] * prices[stock['name']])
    #     old_value += (stock['shares'] * stock['price'])

    # print("Your portfolio is worth ${}, it has changed by ${}".format(
    #     total_value, (total_value - old_value))
