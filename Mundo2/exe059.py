# Menu
n1 = float(input('\nDigite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
r = 0
oper = 0
print('\nDigite:')
print('\n[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')

while oper != 5:
    oper = int(input('\nOperação desejada: '))

    if oper == 1:
        r = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {r}.')

    if oper == 2:
        r = n1 * n2
        print(f'{n1} vezes {n2} é igual a {r}.')

    if oper == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        if n2 > n1:
            print(f'{n2} é maior que {n1}.')
        if n1 == n2:
            print(f'{n1} é igual a {n2}. ')

    if oper == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print('\nDigite:')
        print('\n[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
        oper = int(input('\n'))

print('Fim do programa.')
