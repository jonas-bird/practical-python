# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=','):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            # Read the file headers
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            # TODO fix this so it handles being given colnames that are not in the CSV
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row:     # Skip rows with no data
                continue
            # if type data for the rows was specified in the function call
            # typcast the row accordingly
            if types:
                # I am not sure if we are supposed to do this error check but...
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError:
                     print(f'Row {rowno}: Bad row: {row}')
                     continue

            # if the CSV file has headers create a dictionary using them
            if has_headers:
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]

                record = dict(zip(headers, row))
            # if the CSV file does not have headers create a tuple from each row
            else:
                record = tuple(row)

            # add the row to a list
            records.append(record)

    return records
