# report.py
#
# Exercise 2.4
# import csv
from fileparse import parse_iterable
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Read a portfolio file into a list of stock instances
    '''
    with open(filename) as lines:
        portfolio = Portfolio.from_csv(lines)
    
    return portfolio

def read_prices(filename):
    '''
    Read a file of stock prices into a dictionary
    '''
    with open(filename) as lines:
        return dict(parse_iterable(lines, types=[str, float], has_headers=False))

def portfolio_value(portfolio, prices):
    '''Compute the gain/loss of the portfolio given the prices'''
    value = 0.0

    for stock in portfolio:
        name = stock.name
        shares = stock.shares
        price = stock.price

        try:
            diff = prices[name] - price
            value += shares * diff
            print(name, shares, price, prices[name], f'{diff:0.2f}', f'{(shares * diff):0.2f}')
        except KeyError:
            pass

    return value

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        try:
            report.append((stock.name, stock.shares, prices[stock.name], prices[stock.name] - stock.price))
        except KeyError:
            pass

    return report

def print_report(report, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        formatted_price = '$' + str(f'{price:0.2f}')
        rowdata = [name, str(shares), formatted_price, f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfile, pricefile, fmt='txt'):
    '''
    Make stock report given the portfolio and price files.
    '''
    # Read data files
    portfolio = read_portfolio(portfile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    #Format and print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile format')

    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)


