# Números Primos
print('='*10,'Números Primos','='*10)

n = int(input('Digite um número: '))
c = 0

for d in range(1, n + 1):

    if n % d == 0:
        c += 1       # Contador de divisores (números primos tem 2 divisores)

if c == 2:
    print(f'\nO número {n} é um número primo. \nPois seus divisores são 1 e ele mesmo.')

else:
    print(f'\nO número {n} não é um número primo. \nPois ele tem mais de 2 dois divisores, no caso {c}.')
