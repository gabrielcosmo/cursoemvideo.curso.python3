import random
nome = input('Como é o seu nome ? ')
#print(f'É um grande prazer te conhecer {nome}')

a = random.randint(0,10)

if a == 1:
    print(f'Olá {nome} !')

if a == 2:
    print(f'É um grande prazer em te conhecer, {nome}.')

if a == 3:
    print(f'Oi {nome}.')

else:
    print(f'Prazer {nome}.')
