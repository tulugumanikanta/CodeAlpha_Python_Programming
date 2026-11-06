
print('================================================')
print('            Stock Portfolio Tracker')
print('================================================')

# Available stocks and prices
stocks = {
    'AAPL': 180,
    'TSLA': 250,
    'GOOGL': 150,
    'MSFT': 400,
    'AMZN': 200
}

for stock, price in stocks.items():
    print('Available stock:', stock, '| Price:', price)

# Empty portfolio and initial total
portfolio = {}
total_value = 0

while True:
    stock_symbol = input('\nEnter a stock symbol (or DONE): ').upper()

    if stock_symbol == 'DONE':
        print('\n=========== Portfolio Summary ===========')

        with open('portfolio_summary.txt', 'w') as file:
            file.write('=========== Portfolio Summary ===========\n')

            for symbol, quantity in portfolio.items():
                stock_price = stocks[symbol]
                investment_value = stock_price * quantity

                print('Stock:', symbol)
                print('Quantity:', quantity)
                print('Price per share:', stock_price)
                print('Investment value:', investment_value)

                file.write('Stock: ' + symbol + '\n')
                file.write('Quantity: ' + str(quantity) + '\n')
                file.write('Price per share: ' + str(stock_price) + '\n')
                file.write('Investment value: ' + str(investment_value) + '\n\n')

            print('Total value:', total_value)
            file.write('Total value: ' + str(total_value) + '\n')

        print('Portfolio summary saved successfully.')
        break

    elif stock_symbol in stocks:
        try:
            quantity = int(input('Enter a quantity: '))

            if quantity > 0:
                if stock_symbol in portfolio:
                    portfolio[stock_symbol] += quantity
                else:
                    portfolio[stock_symbol] = quantity

                stock_price = stocks[stock_symbol]
                investment_value = stock_price * quantity
                total_value += investment_value

                print('Stock:', stock_symbol)
                print('Quantity:', quantity)
                print('Price per share:', stock_price)
                print('Investment value:', investment_value)

            else:
                print('Please enter a quantity greater than 0.')

        except ValueError:
            print('Please enter a valid number.')

    else:
        print('Please enter a valid stock symbol.')
