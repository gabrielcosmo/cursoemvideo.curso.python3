#Comparando dois números

n1 = float(input('\nDigite um primeiro valor: '))
n2 = float(input('\nDigite um segundo valor: '))
print('='*30)

if n1 > n2:
    print(f'\nO valor {n1} é maior que o valor {n2}.')

if n2 > n1:
    print(f'\nO valor {n2} é maior que o valor {n1}.')

if n1 == n2:
    print(f'\n{n1} e {n2} são iguais.')
