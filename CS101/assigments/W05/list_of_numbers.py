list_of_numbers = []
chose = -1
largest = 0
positives = []

print('Enter a list of numbers, type 0 when finished.')
while chose != 0:
    chose = int(input('Enter number: '))
    list_of_numbers.append(chose)

list_of_numbers.pop(-1)
list_of_numbers.sort()

positives = {x for x in list_of_numbers if x > 0}

print(f'The sum is: {sum(list_of_numbers)}')
print(f'The average is: {sum(list_of_numbers)/len(list_of_numbers)}')
print(f'The largest number is: {max(list_of_numbers)}')
print(f'The smallest positive number is: {min(positives)}')
print('The sorted list is: ')

# while i < len(list_of_numbers):
#     print(list_of_numbers[i])
#     i += 1

for i in list_of_numbers:
    print(i)