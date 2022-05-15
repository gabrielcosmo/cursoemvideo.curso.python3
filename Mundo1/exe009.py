# Tabuada de um número

print('======= Tabuada=======')

n = int(input('Digite um número: '))
print()

a1 = n * 1
a2 = n * 2
a3 = n * 3
a4 = n * 4
a5 = n * 5
a6 = n * 6
a7 = n * 7
a8 = n * 8
a9 = n * 9
a10 = n * 10

print(f'''{n} x 1 = {a1:2}
{n} x 2 = {a2:2}
{n} x 3 = {a3:2}
{n} x 4 = {a4:2}
{n} x 5 = {a5:2}
{n} x 6 = {a6:2}
{n} x 7 = {a7:2}
{n} x 8 = {a8:2}
{n} x 9 = {a9:2}
{n} x 10 = {a10}''')       # Usar {:2} para colacar o resultado em dois dígitos
