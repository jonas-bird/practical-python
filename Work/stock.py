#!/usr/bin/env python3

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
