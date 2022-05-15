# lista de utilidadesCeV
lista_geral = []
lista_p = []
lista_mais_mag = []
lista_mais_pesada = []
lista_a = [0, 1]
nome = peso = 0

while True:
    if len(lista_p) == 0:
        lista_p.append(str(input('\nNome: ').capitalize().strip()))
        lista_p.append(int(input('Peso: ')))

    else:
        lista_p[0] = str(input('\nNome: ').capitalize().strip())
        lista_p[1] = int(input('Peso: '))

    lista_geral.append(lista_p[:])  # colocando uma cópia dos valores da lista_p na lista_geral

    res = str(input('Deseja continuar: [sim/não] ')).strip()[0]
    while res not in 'sn':
        res = str(input('Deseja continuar ? [sim/não] ')).strip()[0]
    print('.'*30)

    if res == 'n':
        break

for dado1 in range(0, len(lista_geral)):  # selecionando as pessoas mais magras

    if lista_geral[dado1][1] < 90:
        lista_a[0] = (lista_geral[dado1][0])
        lista_a[1] = (lista_geral[dado1][1])

        lista_mais_mag.append(lista_a[:])

    elif lista_geral[dado1][1] >= 90:    # selecionando as pessoas mais pesadas
        lista_a[0] = (lista_geral[dado1][0])
        lista_a[1] = (lista_geral[dado1][1])

        lista_mais_pesada.append(lista_a[:])

print(f'\033[1mForam cadastradas {len(lista_geral)} pessoas ao total.\033[m\n')

if len(lista_mais_mag) > 0:  # print - pessoas mais magras

    if len(lista_mais_mag) == 1:
        print(f'\033[1mA pessoa mais magra é {lista_mais_mag[0][0]}, pesando {lista_mais_mag[0][1]} kg.\033[m')

    else:
        print('\033[1mAs pessoas mais magras (menos de 90kg) são:\033[m\n')

        for r1 in range(0,len(lista_mais_mag)):
            print(f'{lista_mais_mag[r1][0]} com {lista_mais_mag[r1][1]}kg.')

if len(lista_mais_pesada) > 0:  # print - pessoas mais pesadas

    if len(lista_mais_pesada) == 1:
        print(f'\n\033[1mA pessoa mais pesada é {lista_mais_pesada[0][0]}, pesando {lista_mais_pesada[0][1]} kg.\033[m')

    else:
        print('\n\033[1mAs pessoas mais pesadas (mais de 90kg) são:\033[m\n')

        for r1 in range(0, len(lista_mais_pesada)):
            print(f'{lista_mais_pesada[r1][0]} com {lista_mais_pesada[r1][1]}kg.')
