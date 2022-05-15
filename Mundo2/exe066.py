# Interrompendo com o flag
soma = cont = 0
while True:
    n = int(input('\nDigite um número [pare digitando 999]: '))

    if n == 999:
        break
    soma += n
    cont += 1
print('='*40)
print(f'A soma entre todos os {cont} é igual a {soma}')
