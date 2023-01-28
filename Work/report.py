#!/usr/bin/env python3
"""
  report.py
  Exercise 2.4 practical python
  this version typed up by Jonas Bird late 2021 - early 2022
"""
import fileparse
import stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename):
    """recieves a filename for a csv file and returns list of dictionaries with keys: name, share, price"""
    stock_portfolio = []
    colNames = ['name', 'shares', 'price']
    colTypes = [str, int, float]
    with open(filename) as f:
        stock_dicts = fileparse.parse_csv(f, colNames, colTypes)
    stock_portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for
                        d in stock_dicts ]
    return Portfolio(stock_portfolio)


def read_prices(filename):
    """reads a list of stock symbols and prices from a csv file and returns
    a dictionary with the stock symbol as key and the price as value"""
    stock_prices = {}
    with open(filename) as f:
        stock_list = fileparse.parse_csv(f, None, [str, float], False)
    for stock_name, price in stock_list:
        stock_prices[stock_name] = price
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


def print_report(stock_report, formatter):
    """
    format and output a table from a list (name, shares, price, change)
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in stock_report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(holdings_file, prices_file, output_format='txt'):
    """
    Make a stock report from a portfolio and price data files.
    """
    # read the data from provided files
    stocks = read_portfolio(holdings_file)
    prices = read_prices(prices_file)
    # Create the report data
    report = make_report(stocks, prices)
    # print the report
    formatter = tableformat.create_formatter(output_format)
    print_report(report, formatter)


def main(argv):
    if len(argv) == 4:
        holding_file = argv[1]
        price_file = argv[2]
        output_format = argv[3]
    else:
        holding_file = 'Data/portfolio.csv'
        price_file = 'Data/prices.csv'
        output_format = 'txt'
        print('Usage: %s portfile pricefile format' % argv[0])
        print("Using default testing values")
    portfolio_report(holding_file, price_file, output_format)


if __name__ == '__main__':
    import sys
    main(sys.argv)
