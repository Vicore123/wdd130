secret_word = 'mosiah'
user_guess = ''
hints = 1

print('\nWelcome to the word guessing game!\n')

while user_guess != secret_word:

    user_guess = input('What is your guess? ').lower()
    if user_guess == secret_word:
        print(f'Congratulations! You guessed it! \nIt took you {hints} guesses.')
    else:
        print('Your guess was not correct.')
        hints += 1