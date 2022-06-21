#!/usr/bin/env python3 
"""
Code from practical python course
https://dabeaz-course.github.io/practical-python/
"""
import os
import time
import report


def follow(aFile):
    # generator that produces lines from a file
    f = open(aFile)
    f.seek(0, os.SEEK_END)  # Move file handle to end of file
    while True:
        newLine = f.readline()
        if newLine == '':
            time.sleep(0.1)
            continue
        yield newLine


if __name__ == '__main__':

    portfolio = report.read_portfolio('Data/portfolio.csv')
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('""')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
