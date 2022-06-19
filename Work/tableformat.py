#!/usr/bin/env python3
"""
Class to define output formats for use with report.py
Part of exercise 4.4 from Practical Python
Typed up by Jonas Bird
2022-04-23
"""


class FormatError(Exception):
    """
    Indicate that create_formatter dose not have a formatter that matches
    the string it recieved
    """
    pass


class TableFormatter:
    """
    Abstract base class
    """
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=" ")
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio as CSV format
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio as a HTML table
    """
    def headings(self, headers):
        print("<tr><th>" + "</th><th>".join(headers) + "</th></tr>")

    def row(self, rowdata):
        print("<tr><td>" + "</td><td>".join(rowdata) + "</td></tr>")


def create_formatter(name):
    """
    Return the appropriate type of formatter based on an input text string
    """
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')

    return formatter


def print_table(objects, attributes, formatter):
    """
    From a collection of objects, a list of attributes, and a formatter
    print a table with columns of the provided attributes and each row
    one of the
    """
    formatter.headings(attributes)
    for o in objects:

        row_data = []
        for a in attributes:
            row_data.append(str(getattr(o, a)))
        formatter.row(row_data)
