word = 'commitment'
favorite_letter = input('What is your favorite letter? ').lower()

for letter in word:
    if letter == favorite_letter:
        print('_', end='')
    else:
        print(letter.lower(), end='')