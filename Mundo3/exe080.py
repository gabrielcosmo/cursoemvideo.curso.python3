# Ordem crescente de 5 valores  sem o sort()
lista_num = []

for c in range(0, 5):
    n = int(input(f'\nDigite um valor: '))

    if c == 0 or n > lista_num[-1]:
        lista_num.append(n)
        print(f'O valor {n} foi adicionado na última posição.')
    else:
        pos = 0
        while pos <= len(lista_num):

            if n < lista_num[pos]:
                lista_num.insert(pos, n)
                print(f'O valor {n} foi aidcionado na posição {pos}.')
                break
            pos += 1
print(f'='*30)
print(f'Os valores em Ordem crescente são: {lista_num}')
