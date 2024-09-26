import math

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))

subtotal = (child_meal * children) + (adult_meal * adults)
print(f'\nSubtotal: ${subtotal}')

tax_rate = float(input('\nWhat is the sales tax rate? '))
sales_tax = round(subtotal * tax_rate / 100, 2)
print(f'Sales Tax: ${sales_tax}')

total_price = round(subtotal + sales_tax, 2)
print(f'Total: ${total_price}')

payment_amount = float(input('\nWhat is the payment amount? '))

change = payment_amount - total_price
print(f'Change: ${change}')