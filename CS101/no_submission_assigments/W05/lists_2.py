shopping_list = []
new_item = ''

print('Please enter the items of the shopping list (type: quit to finish):')

while new_item != 'quit':
    new_item = input('Item: ').lower()

    if new_item != 'quit':
        shopping_list.append(new_item)


print('\nThe shopping list is: ')

for item in shopping_list:
    print(item)


print('\nThe shopping list with indexes is:')

for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')

print()

index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')
shopping_list[index] = new_item


print('\nThe shopping list with indexes is:')

for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')