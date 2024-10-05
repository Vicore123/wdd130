number1 = int(input('Give me a number: '))
number2 = int(input('Give me another number: '))

if number1 > number2:
    print('The first number is greater')
else:
    print('The first number is not greater')

if number1 == number2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if number2 > number1:
    print('The second number is greater')
else:
    print('The second number is not greater')

print() #separator

animal = input('What is your favorite animal? ')

if animal.lower() == 'dog':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')