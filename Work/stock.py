#!/usr/bin/env python3
"""
Defines a stock class that represents a position in an stock portfolio
Part of Chapter 4 assignments in Practical Python
"""
from typedproperty import typedproperty

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        """Initialize a stock with the stock's:
        name, number of shares, and price per share
        """
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price:0.2f})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares_to_sell):
        self.shares -= shares_to_sell
