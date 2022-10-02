import random

# Crie uma lista com o nome de 10 pessoas e sorteie uma pessoa, depois embaralhe novamente e sorteie outra (sem repetição).

lista = ['Rian', 'Carlos', 'Bianca', 'Gabriel', 'Eloisa', 'Luciana', 'Edmilson', 'Luzinete', 'Elisângela', 'Tânia']
escolhido = random.choice(lista)
print('Escolhido foi: {}'.format(escolhido))

# Faça um programa que permita ao usuário digitar o nome e em seguida mostrar ao usuário de trás pra frente somente em letras maiúsculas.

nome = input('Informe o seu Nome: ')
rev = nome[::-1]
print(rev.upper())
