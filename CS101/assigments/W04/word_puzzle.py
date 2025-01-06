# I put the counter 'max_hints' to count the number of attempts, to do so, I put another parameter in the while loops to check 
# if there is still any attempts left. this variable and the secret_word may be changed.

secret_word = 'mosiah'
user_guess = ''
for letter in secret_word:
    user_guess += ' '
hints = 0
max_hints = 5

print('\nWelcome to the word guessing game!\n')

while user_guess != secret_word and max_hints > 0:

    print('Your hint is: ', end='')
    for letter in range(len(secret_word)):

        if secret_word[letter] ==  user_guess[letter]:
            print(f'{user_guess[letter].upper()} ', end='')
        elif user_guess[letter] in (secret_word):
            print(f'{user_guess[letter]} ', end='')
        else:
            print('_ ', end='')

    user_guess = input(f'\nWhat is your guess? ({max_hints} guesses left) ').lower()
    hints += 1
    max_hints -= 1

    while len(user_guess) != len(secret_word) and max_hints > 0:
        user_guess = input(f'Sorry, the guess must have the same number of letters as the secret word.\n\nWhat is your guess? ({max_hints} guesses left) ').lower()
        hints += 1
        max_hints -= 1

if user_guess == secret_word:
    print(f'Congratulations! You guessed it! \nIt took you {hints} guesses.')
else:
    print("I'm sorry, the number of guesses is over")