#Parte inteira de um número
from math import trunc

n = float(input('Digite um número e veja sua parte inteira: '))
par_int = trunc(n)

print(f'\nA parte ineira de {n} é {par_int}.')
