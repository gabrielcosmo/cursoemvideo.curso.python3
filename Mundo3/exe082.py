# Listas com Pares e Impares
lista_num = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('\nDigite um valor: '))
    while valor in lista_num:
        valor = int(input(f'\nDigite um valor [valor {valor} já está na lista, digite outro número]: '))

    lista_num.append(valor)
    print(f'Valor {valor} já adicionado...')

    res = str(input('\nQuer continuar ? [sim/não] ')).lower()[0]
    while res not in 'sn':
        res = str(input('\nQuer continuar ? [sim/não] ')).lower()[0]

    if res == 'n':
        break

for n in lista_num:

    if n % 2 == 0:
        lista_par.append(n)

    else:
        lista_impar.append(n)

print('.' * 50)
print(f'Os valores digitados foram: {sorted(lista_num)}')
print(f'Os valores pares são: {lista_par}')
print(f'Os valores ímpares são: {lista_impar}')
