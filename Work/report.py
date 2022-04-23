#!/usr/bin/env python3

# report.py
# Exercise 2.4 practical python
# this version typed up by Jonas Bird late 2021 - early 2022

import fileparse
import stock


def read_portfolio(filename):
    """recieves a filename for a csv file and returns list"""
    stock_portfolio = []
    colNames = ['name', 'shares', 'price']
    colTypes = [str, int, float]
    with open(filename) as f:
        stock_dicts = fileparse.parse_csv(f, colNames, colTypes)
    stock_portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for
                        d in stock_dicts ]
    return stock_portfolio


def read_prices(filename):
    """reads a list of stock symbols and prices from a csv file and returns
    a dictionary with the stock symbol as key and the price as value"""
    stock_prices = {}
    with open(filename) as f:
        stock_list = fileparse.parse_csv(f, None, [str, float], False)
    for stock_name, price in stock_list:
        stock_prices[stock_name] = price
    # with open(filename, 'r') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         try:
    #             stock_prices[row[0]] = float(row[1])
    #         except:
    #             continue

    return stock_prices


def make_report(stock_list, prices_dict):
    """takes a list of Stock objects as defined by stock.Stock representing
    stock holdings and a dictionary of stock symbols and the current price and
    returns a list of tuples"""
    stock_status = []
    for stock_symbol in stock_list:
        stock_info = (
            stock_symbol.name,
            stock_symbol.shares,
            float(prices_dict[stock_symbol.name]),
            float(prices_dict[stock_symbol.name] - stock_symbol.price)
        )
        stock_status.append(stock_info)
    return stock_status


def print_report(stock_report):
    """format and print the data in a nice tabulated way"""
    # output the report generated in make_report
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in stock_report:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(holdings_file, prices_file):
    """calls other functions instead of a main function I guess"""
    stocks = read_portfolio(holdings_file)
    prices = read_prices(prices_file)
    print_report(make_report(stocks, prices))


def main(argv):
    if len(argv) == 3:
        holding_file = argv[1]
        price_file = argv[2]
    else:
        holding_file = 'Data/portfolio.csv'
        price_file = 'Data/prices.csv'

    portfolio_report(holding_file, price_file)


if __name__ == '__main__':
    import sys
    main(sys.argv)
