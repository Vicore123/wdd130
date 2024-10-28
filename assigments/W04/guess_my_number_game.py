import random
decision = 'yes'

while decision == 'yes':
    number = random.randint(1, 100)
    guess = int()
    count = 0

    while guess != number:

        guess = int(input('What is your guess? '))
        count += 1

        if number < guess:
            print('Lower')
        elif guess < number:
            print('Higher')
        else:
            print('You guessed it!')

    print(f'It took you {count} guesses')
    decision = input('would you like do play again? (yes, no) ').lower()

print('Thank you for playing!! :)')