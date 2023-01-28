#!/usr/bin/env python3

"""
Exercise from practical python
https://dabeaz-course.github.io/practical-python/
"""

import csv
from follow import follow


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parse_stock_data(lines_in):
    csv_rows = csv.reader(lines_in)
    csv_rows = select_columns(csv_rows, [0, 1, 4])
    return csv_rows


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
