# Lendo vérios valores
x = 1
lista_num = []
while True:
    valor = int(input(f'\nDigite o {x}º valor: '))

    while valor in lista_num:
        valor = int(input(f'\nDigite {x}º valor [valor {valor} já está na lista, digite outro número]: '))

    lista_num.append(valor)

    print(f'Valor {valor} já adicionado...')

    res = str(input('\nQuer continuar ? [sim/não] ')).lower()[0]
    while res not in 'sn':
        res = str(input('\nQuer continuar ? [sim/não] ')).lower()[0]
    x += 1

    if res == 'n':
        break
print(f'.'*50)
print(f'Foram digitados {len(lista_num)} valores.')
print(f'Ordem decrescente de valores: {sorted(lista_num,reverse=True)}')

if 5 in lista_num:
    print(f'Temos o número 5 na lista de valores.')

else:
    print('O valor 5 não foi declarado.')
