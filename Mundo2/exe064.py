# Lendo vários números até o flag - número de parada - 999

n = 0
soma = cont = 0

print('\nDigite vários números e veja a soma entre eles [pare digitando 999]:\n')

while n != 999:
    n = int(input(''))

    if n != 999:
        soma = soma + n
        cont += 1
print(f'\nA soma de todos os {cont} digitados é igual a {soma}')
