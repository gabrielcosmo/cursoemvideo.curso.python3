# Somando números pares
soma = 0
teste = 0

print('\nDigite 6 números, e veja a soma dos pares entre eles:\n')

for x in range(1, 7):
    n = int(input(f'Digite o {x} valor: '))

    if (n % 2) == 0:
        soma += n
        teste += 1

if teste >= 1:
    print(f'\nA soma dos números pares é igual a {soma}')

if teste == 0:
    print('\nNão foram digitados números pares.')
