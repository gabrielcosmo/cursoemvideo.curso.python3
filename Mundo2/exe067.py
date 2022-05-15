# Tabuada com while True
n = mult = 0
fator = 1
print('='*10,'Tabuada','='*10)
while True:

    n = int(input('\nDigite um número e veja sua tabuada: '))
    print('-'*30)
    if n < 0:
        break

    while fator <= 10:
        mult = n * fator
        print(f'{n} x {fator:2} = {mult}')
        fator += 1

    print('-'*30)
    print('[pare digitando um número negativo]')
    fator = 1
print('Fim do programa.')
