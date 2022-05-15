# Tupla - Lendo um número de 0 a 20
tup_0_20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('\nDigite um número inteiro de 0 a 20: '))

while n < 0 or n > 20:
    print(f'\n{n} está fora do intervalo de 0 a 20.\nTente novamente.\n')
    n = int(input('Digite um número inteiro de 0 a 20: '))

print('='*(13 + len(tup_0_20[n])))
print(f'Você digitou \033[7m{tup_0_20[n]}\033[m.')
