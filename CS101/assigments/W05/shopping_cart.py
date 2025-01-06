# I fixed the position of the prices in columns, so when they are displayed, the prices are aligned. You can change the formatting size using the variable 'formatting_len'.

chose = ''
shopping_list = []
prices = []
formatting_len = 10
formatting = ''

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
            formatting = ''
            for j in range(formatting_len - len(shopping_list[i])):
                formatting += ' '

            print(f"{i+1}. {shopping_list[i]} {formatting}-    ${prices[i]:.2f}")
        print()

    elif chose == 3:
        print('The contents of the shopping cart are:')
        for i in range(len(shopping_list)):
            formatting = ''
            for j in range(formatting_len - len(shopping_list[i])):
                formatting += ' '

            print(f"{i+1}. {shopping_list[i]} {formatting}-    ${prices[i]:.2f}")

        remove_item = int(input('\nWhich item would you like to remove? '))
        if 0 <= remove_item - 1 < len(shopping_list):
            shopping_list.pop(remove_item - 1)
            prices.pop(remove_item - 1)
            print('Item removed.')
        
        else:
            print('Sorry, that is not a valid item number.')
    
    elif chose == 4:
        print(f'The total price of the items in the shopping cart is ${sum(prices):.2}\n') 
    
    elif chose == 5:
        print('Thank you. Goodbye.')
    
    else:
        print('Please, enter a valid number')
