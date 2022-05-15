# Matriz 3x3 -  v2.0
lista_col0 = [] # apenas números de referencia
lista_col1 = []
lista_col2 = []
lista_matriz = [lista_col0, lista_col1, lista_col2]
n = pos = soma_par = soma_ter_col = 0
y1 = y2 = y3 = 0

for n in range(0,3):
    if n == 0:
        for x in range(0,3):
            pos = int(input(f'Digite um número para a posição ({n},{y1}): '))
            lista_matriz[0].append(pos)
            y1 += 1

    elif n == 1:
        for x in range(0,3):
            pos = int(input(f'Digite um número para a posição ({n},{y2}): '))
            lista_matriz[1].append(pos)
            y2 += 1

    elif n == 2:
        for x in range(0, 3):
            pos = int(input(f'Digite um número para a posição ({n},{y3}): '))
            lista_matriz[2].append(pos)
            y3 += 1

print('.'*40)
print('Matriz:')
for p in range(0,len(lista_matriz)):
    for p2 in lista_matriz[p]:
        print(f'\033[1m{p2:^5}\033[m', end='')
    print('')

for s in range(0,len(lista_matriz)):

    for s2 in lista_matriz[s]:
        if s2 % 2 == 0:
            soma_par += s2

for s in lista_matriz[2]:
    soma_ter_col += s

print('.'*40)
print(f'A soma dos valores pares é igual a {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_ter_col}.')
print(f'O maior valor da segunda coluna é {max(lista_matriz[1])}.')
