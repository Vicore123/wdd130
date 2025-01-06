# I added the possibility to choose exactly what you want to calculate using the while structure, and I added the drink section as well

child_meal = 0
children = 0
adult_meal = 0
adults = 0
drinks = 0
drinks_quantity = 0


print('\nPlease enter the desired option:')
print('1- child_meal \n2- adult_meal \n3- drink \n')
choose = int(input())

while (choose != 0):

    if (choose == 1):
        child_meal = float(input("What is the price of a child's meal? $"))
        children = int(input('How many children are there? '))
        choose = int(input('\nSomething else? \n1- child meal \n2- adult meal \n3- drink \n(type 0 to finish)\n(selecting a already selected option will overwrite it)\n'))

    if (choose == 2):
        adult_meal = float(input("What is the price of an adult's meal? $"))
        adults = int(input('How many adults are there? '))
        choose = int(input('\nSomething else? \n1- child meal \n2- adult meal \n3- drink \n(type 0 to finish)\n(selecting a already selected option will overwrite it)\n'))

    if (choose == 3):
        drinks = float(input("What is the price of a drink? $"))
        drinks_quantity = int(input('How many drinks? '))
        choose = int(input('\nSomething else? \n1- child meal \n2- adult meal \n3- drink \n(type 0 to finish)\n(selecting a already selected option will overwrite it)\n'))


subtotal = (child_meal * children) + (adult_meal * adults) + (drinks * drinks_quantity)
print(f'\nSubtotal: ${subtotal}')

tax_rate = float(input('\nWhat is the sales tax rate? (enter whole number) '))
sales_tax = round(subtotal * tax_rate / 100, 2)
print(f'Sales Tax: ${sales_tax}')

total_price = round(subtotal + sales_tax, 2)
print(f'Total: ${total_price}')

payment_amount = float(input('\nWhat is the payment amount? $'))

change = payment_amount - total_price
print(f'Change: ${change}')