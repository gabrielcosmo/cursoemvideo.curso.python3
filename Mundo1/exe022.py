# Lendo um Nome
import time
s = 0
nome = str(input('Seu nome completo: '))

maius = nome.upper()
minus = nome.lower()

nome_div = nome.split()

for x in range(0,len(nome_div)):
    s += len(nome_div[x])

p_nome = len(nome_div[0])

print('\nAnalisando...')
time.sleep(3)

print('-'*40)
print(f'\nSeu nome só letras maiúsculas: {maius}')
print(f'\nSeu nome só com letras minúsculas: {minus}')
print(f'\nNúmero de caracteres (sem espaços): {s}')
print(f'\nNúmero de caracteres no seu primeiro nome: {p_nome}')
