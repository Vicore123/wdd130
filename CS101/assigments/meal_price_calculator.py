child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))

subtotal = (child_meal * children) + (adult_meal * adults)
print(f'\nSubtotal: ${subtotal}')

tax_rate = float(input('\nWhat is the sales tax rate? '))
sales_tax = subtotal * tax_rate / 100
print(f'Sales Tax: ${sales_tax:.2f}')

total_price = subtotal + sales_tax
print(f'Total: ${total_price:.2f}')

payment_amount = float(input('\nWhat is the payment amount? '))

change = payment_amount - total_price
print(f'Change: ${change:.2}')