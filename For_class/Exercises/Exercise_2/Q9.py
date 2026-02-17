'''Write a program that takes as input the cost price and selling price of an item, prints whether
the sale resulted in a profit or a loss, and prints the amount.'''

cost_price = float(input("What is the cost price: "))
selling_price = float(input("What is the selling price: "))
if selling_price > cost_price:
    print(f'Profit is {(selling_price - cost_price):.2f}')
elif selling_price < cost_price:
    print(f'Loss is {(cost_price - selling_price  ):.2f}')
else:
    print("Sold for cost price so neither price nor loss")