noun = input('noun: ')
condition = list(noun)[0]
article = 'a'
if (condition == 'a' or condition == 'e' or condition == 'i' or condition == 'o' or condition == 'u'):
    article = 'an'
print(f'{article} {noun}')