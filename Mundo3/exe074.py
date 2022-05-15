# Sorteando números e adicionando a Tupla
import random
t = (random.randint(0, 10),
     random.randint(0, 10),
     random.randint(0, 10),
     random.randint(0, 10),
     random.randint(0, 10))

print('\nOs cinco números nessa sequencia são:', end=' ')
for x in t:
    print(x, end=' ')

print(f'\nMaior: {max(t)} \nMenor: {min(t)}')
# max() - maior valor em uma tupla
# min() - menor valor em uma tupla
