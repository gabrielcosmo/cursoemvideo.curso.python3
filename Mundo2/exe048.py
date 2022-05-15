# Soma dos números ímpares múltiplos de 3, de 1 a 500
s = 0
cont = 0
for c in range(1,501):

    if (c % 2) == 1 and (c % 3) == 0:
        cont += 1    # contador
        s += c       # acumulador
print(f'A soma dos {cont} números ímpares múltiplos de 3 entre 1 e 500 é igual a {s}')
