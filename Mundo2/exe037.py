# Conversor de Bases

num = int(input('\nDigite um número inteiro: '))

print('\n1 - Binário \n2 - Octal \n3 - Hexadecimal ')
bas = int(input('\n'))

if bas == 1:
    novo = bin(num)
    print(f'Interio: {num} \nBinário: {novo[2:]}')

elif bas == 2:
    novo = oct(num)
    print(f'Inteiro: {num} \nOctal: {novo[2:]}')

elif bas == 3:
    novo = hex(num)
    print(f'Inteiro: {num} \nHexadecimal: {novo[2:]}')

else:
    print('Opcão inválida. Tente novamente')
