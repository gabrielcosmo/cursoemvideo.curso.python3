# Caixa Eletrônico - saque em cédulas de R$ 50,20,10,1
print('='*10,'Banco','='*10)
valor_saque = int(input('\nValor a ser sacado: '))
total = valor_saque
total_ced = 0
ced = 50
print(f'\nVocê receberá os R$ {valor_saque} em: \n')
while True:

    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'{total_ced} cedélas de R${ced}.')
        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        total_ced = 0

        if total == 0:
            break
print('\n\nFim do processo.\nVolte sempre')
