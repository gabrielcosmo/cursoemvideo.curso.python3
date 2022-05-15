# Adicionando valores a uma lista
valores = []
maior = menor = 0
for v in range(0, 5):
    val = int(input(f'\nDigite o {v + 1}º valor: '))
    valores.append(val)

    if v == 0:
        maior = menor = valores[v]

    else:
        if valores[v] > maior:
            maior = valores[v]

        elif valores[v] < menor:
            menor = valores[v]

print('.'*40)
print(f'\nVocê digitou os valores: {valores}')
print(f'O maior valor é o número {maior}, nas posiçôes: ', end=' ')

for x in range(0, len(valores)):
    if valores[x] == maior:
        print(x, end='...')

print('')
print(f'O menor valor é o número {menor}, nas posiçôes: ', end=' ')

for x in range(0, len(valores)):
    if valores[x] == menor:
        print(x, end='...')
