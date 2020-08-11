class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        HTMLheaders = '<tr>'
        for h in headers:
            HTMLheaders += '<th>' + h + '</th>'
        HTMLheaders += '</tr>'

        print(HTMLheaders)

    def row(self, rowdata):
        r = '<tr>'
        for d in rowdata:
            r += '<td>' + d + '</td>'
        r += '</tr>'

        print(r)

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')

def print_table(objects, headers, formatter):
    '''
    Print a table showing user-specificied attributes of a list of arbitrary objects
    '''
    formatter.headings(headers)

    for row in objects:
        rowdata = [str(getattr(row, colname)) for colname in headers]
        formatter.row(rowdata)

