# Fatorial de um número

n = int(input('\nDigite um número e veja seu fatorial: '))
fator = n - 1
n2 = n
r = 0

if n == 1:
    print('\nO fatorial de 1 é 1.')

while fator > 0:
    print(f'{fator}', end='')
    print(' x ' if fator > 1 else ' = ', end='')
    n2 = n2 * fator
    fator = fator - 1

print(n2, end='')
print(f'\nO fatorial de {n} é igual a {n2}.')
