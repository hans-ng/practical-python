# fileparse.py
#
# Exercise 3.3

import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Raise a RuntimeError exception when select is not None and has_headers=False
        if (select) and (has_headers == False):
            raise RuntimeError('select argument requires column headers')

        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # Get the indices of selected columns specified in the "select" list
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows):
            if not row:     # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Catch all ValueError exceptions for rows that can't be converted
            try:
                # Apply the types to the row
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                 # Make a dictionary or a tuple
                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if silence_errors:
                    continue
                print("Row {0}: Couldn't convert {1}".format(rowno+1, row))
                print("Row {}: Reason {}".format(rowno+1, e))
        
    return records

# A more flexible version of parse_csv
def parse_iterable(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse an iterable object into a list of records
    '''
    rows = csv.reader(lines, delimiter=delimiter)
    
    # Raise a RuntimeError exception when select is not None and has_headers=False
    if (select) and (has_headers == False):
        raise RuntimeError('select argument requires column headers')

    headers = next(rows) if has_headers else []

    # Get the indices of selected columns specified in the "select" list
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows):
        if not row:     # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]

        # Catch all ValueError exceptions for rows that can't be converted
        try:
            # Apply the types to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary or a tuple
            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)
        except ValueError as e:
            if silence_errors:
                continue
            # print("Row {0}: Couldn't convert {1}".format(rowno+1, row))
            # print("Row {}: Reason {}".format(rowno+1, e))
            log.warning("Row %d: Couldn't convert %s", rowno+1, row)
            log.debug("Row %d: Reason %s", rowno+1, e)
        
    return records