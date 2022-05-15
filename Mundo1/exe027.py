#Nome de uma pessoa primeiro e último nome

nome = str(input('\nDigite seu nome: ')).strip()

a = 0
a1 = 0

sep = nome.split()
print(f'\nNome completo: {nome} \nPriemiro nome: {sep[0]} \nÚltimo nome: {sep[len(sep) - 1]}')
