chose = ''
shopping_list = []
prices = []

print('\nWelcome to the Shopping Cart Program!\n')

while chose != 5:
    chose = int(input('Please select one of the following: \n\
1. Add item \n\
2. View cart \n\
3. Remove item \n\
4. Compute total \n\
5. Quit \n\
Please enter an action: '))
    
    if chose == 1:
        new_item = input('What item would you like to add? ')
        shopping_list.append(new_item)
        prices.append(float(input(f"What is the price of '{new_item}'? ")))
        print(f"'{new_item}' has been added to the cart.\n")
    
    elif chose == 2:
        print('The contents of the shopping cart are:')
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i]} - ${prices[i]:.2f}")
        print()

    elif chose == 3:
        print()

    elif chose == 4:
        print() 
    
    elif chose == 5:
        print('Thank you. Goodbye.')
    
    else:
        print('Please, enter a valid number')