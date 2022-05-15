# Adicionando vários valores a um a lista
lista_num = []

while True:
    n = int(input('\nDigite um número: '))

    if n in lista_num:
        while n in lista_num:
            n = int(input(f'\nDigite um número [o valor {n} já foi adicionado, digite outro]: '))

    lista_num.append(n)
    print(f'Valor {n} adicionado...')
    res = str(input('\nQuer continuar: [sim/não] ')).lower()[0]

    while res not in 'sn':
        res = str(input('\nQuer continuar: [sim/não] ')).lower()[0]

    if res == 'n':
        break
print('.' * 45)
print(f'\nOs números digitados em ordem crescente são: {sorted(lista_num)}')
