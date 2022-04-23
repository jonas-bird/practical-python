#!/usr/bin/env python3
"""
Defines a stock class that represents a position in an stock portfolio
Part of Chapter 4 assignments in Practical Python
"""


class Stock:

    def __init__(self, name, shares, price):
        """Initialize a stock with the stock's:
        name, number of shares, and price per share
        """
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares_to_sell):
        self.shares -= shares_to_sell
