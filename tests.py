palavra = 'palavra'
numero = 'numero'
indentacao_length = 10
indentacao = str()


for i in range(indentacao_length - len(palavra)):
    indentacao += ' '


print(f'{palavra}{indentacao}{numero}')

indentacao = ''
for i in range(indentacao_length - len(numero)):
    indentacao += ' '
print(f'{numero}{indentacao}{palavra}')