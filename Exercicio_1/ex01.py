num_1 = int(input('Informe um número inteiro: '))
num_2 = int(input('Informe outro número inteiro: '))
num_3 = float(input('Informe um número real: '))

print()
print('O produto do dobro do primeiro com a metade do segundo: ')
print(f'{(num_1 * 2) + (num_2 / 2)}')
print('A soma do triplo do primeiro com o terceiro: ')
print(f'{(num_1 * 3) + num_3}')
print('O terceiro elevado ao cubo: ')
print(f'{float(pow(num_3, 3))}')