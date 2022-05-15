# Lista de pares e impares
lista_par = []
lista_impar = []
lista_num = [lista_par, lista_impar]
for n in range(0, 7):
    valor = int(input(f'Digite o {n + 1}º número: '))
    print('.'*21)
    if valor % 2 == 0:
        lista_num[0].append(valor)
    else:
        lista_num[1].append(valor)

print(f'Os valores pares digitados foram: {sorted(lista_num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista_num[1])}')
