# Matriz 3x3 com listas

lista_col0 = [] # apenas números de referencia
lista_col1 = []
lista_col2 = []
lista_matriz = [lista_col0, lista_col1, lista_col2]
n = 0
pos = 0
y1 = y2 = y3 = 0

for n in range(0, 3):
    if n == 0:
        for x in range(0, 3):
            pos = int(input(f'Digite um número para a posição ({n},{y1}): '))
            lista_matriz[0].append(pos)
            y1 += 1

    elif n == 1:
        for x in range(0, 3):
            pos = int(input(f'Digite um número para a posição ({n},{y2}): '))
            lista_matriz[1].append(pos)
            y2 += 1

    elif n == 2:
        for x in range(0, 3):
            pos = int(input(f'Digite um número para a posição ({n},{y3}): '))
            lista_matriz[2].append(pos)
            y3 += 1

print('.'*30)
print('Matriz:')
for p in range(0,len(lista_matriz)):
    for p2 in lista_matriz[p]:
        print(f' \033[1m{p2:^5}', end='')
    print('')
