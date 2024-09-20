# I added the possibility of the article change according to the noun inputed, if it starts with vogal it will be 'an' otherwise it
# will be 'a'. On the last 2 prints I also added more story and the use of .title() as movie name. Hope you enjoy it :)

print('\nPlease enter the following:\n')

adjective1 = input('adjective: ')
animal1 = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
adjective2 = input('adjective: ')
place = input('place: ')
noun = input('noun: ')
condition = list(noun)[0]
article = 'a'
if (condition == 'a' or condition == 'e' or condition == 'i' or condition == 'o' or condition == 'u'):
    article = 'an'
movie = input('Sentence: ')
animal2 = input('animal: ')

print('\nYour story is:\n')

print(f'The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective1} {animal1} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print(f'right in front of my family.')
print(f'After that {adjective2} experience, I went to {place} and ate {article} {noun}.')
print(f'If I had more time, I would watch the movie "{movie.title()}" with my {animal2}.')