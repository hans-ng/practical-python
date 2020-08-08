# pcost.py
#
# Exercise 1.27
# import csv
import sys
import report

def portfolio_cost(filename):
    '''
    Calculate the total cost of the portfolio from a csv file
    '''
    portfolio = report.read_portfolio(filename)

    return sum([stock.shares * stock.price for stock in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])

    cost = portfolio_cost(args[1])
    print(f'Total cost {cost:0.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)