# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None,
        has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select is not None and has_headers is False:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            # Read the file headers
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
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
                # I was not sure if I was supposed to do this error check
                # it ended up being added in next chapter!
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if silence_errors is False:
                        print(f'Row {rowno}: Bad row: {row}')
                        print("Reason ", e)
                    continue

            # if the CSV file has headers create a dictionary using them
            if has_headers:
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]

                record = dict(zip(headers, row))
            # if the file does not have headers create a tuple from each row
            else:
                record = tuple(row)

            # add the row to a list
            records.append(record)

    return records
