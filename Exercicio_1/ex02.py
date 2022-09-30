lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print('Lista Completa: ')
print(lista)
print()
print('Intervalo 1 a 9: ')
print(lista[1:9])
print()
print('Intervalo de 8 a 13: ')
print(lista[8:13])
print()
print('Números Pares: ')
for pares in lista:
    if pares % 2 == 0:
        print(pares)
print()
print('Números Ímpares: ')
for impares in lista:
    if not impares % 2 == 0:
        print(impares)
        
print()
print('Múltiplos de 2, 3 e 4: ')
for multiplos in lista:
    if multiplos % 2 == 0 and multiplos % 3 == 0 and multiplos % 4 == 0:
        print(multiplos)
print()
print('Lista Reversa: ')
rev = lista[::-1]
print(rev)
print()
print('A razão entre a soma do Intervalo de 10 a 15 pelo Intervalo de 3 a 9 em float: ')
soma_1 = lista[10:15]

