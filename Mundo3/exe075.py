# Lendo quatro números e colocando em uma tupla

t = (int(input('\nDigite o primeiro número: ')),
     int(input('\nDigite o primeiro número: ')),
     int(input('\nDigite o primeiro número: ')),
     int(input('\nDigite o primeiro número: ')))

cont = 0
print('='*20)
print(f'Temos os números: {t}')

if t.count(9) == 0:    # se há o número 9
    print('Nenhum número 9 na sequencia.')
else:
    print(f'\nO número 9 aparece {t.count(9)} vezes.')

if 3 in t:  # posição do número 3, se haver o 3
    print(f'\nTemos o número 3 na posição {t.index(3) + 1}.')
else:
    print('\nNão temos o número 3 na sequencia.')

for x in t:
    if x % 2 == 0:
        cont += 1

if cont > 1:
    print('Os números pares são: ', end=' ')

    for x in t:
        if x % 2 == 0:
            print(x, end=' ')

if cont == 1:
    print('O único número par é o ', end=' ')

    for x in t:
        if x % 2 == 0:
            print(x)

if cont == 0:
    print('Não temos números pares.')
