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


def convert_types(rows, types):
    for col in rows:
        yield [func(val) for func, val in zip(types, col)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def parse_stock_data(lines_in):
    csv_rows = csv.reader(lines_in)
    csv_rows = select_columns(csv_rows, [0, 1, 4])
    csv_rows = convert_types(csv_rows, [str, float, float])
    csv_rows = make_dicts(csv_rows, ['name', 'price', 'change'])
    return csv_rows


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
