#Aumento de Salário de um Funcionário

sal = float(input('\nDigite seu salário aqui: R$ '))

if sal > 1250:
    x = sal * (10/100)
    n_sal = sal + x
    print('='*30)
    print(f'\nSeu novo salário é de R$ {n_sal:.2f} \nAumento de: R$ {x:.2f} (10%)')

if sal <= 1250:
    x = sal * (15/100)
    n_sal = sal + x
    print('='*30)
    print(f'\nSeu novo salário é de: {n_sal:.2f} \nAumento de: R$ {x:.2f} (15%)')