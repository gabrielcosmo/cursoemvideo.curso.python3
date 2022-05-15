# Tabuada usando o for

n = int(input('\nDigite um número para ver sua tabuada: '))
print('\n')
print('='*10,'Tabuada','='*10)

for x in range(1, 11):
    m = n * x
    print(f'{n:2} x {x:2} = {m:2}')     # {:2} para colocar em 2 caracteres
