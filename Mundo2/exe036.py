# Aprovando um Empréstimo para a compra de uma casa
import datetime

print('\033[34m=>\033[m'*10,'\033[33mSistema Bancário','\033[34m<='*10)

nome = str(input('\nSeu nome: ')).capitalize().strip()
conta = str(input('\nInforme o número da sua conta: ')).strip()
v_casa = float(input('\nValor do Imóvel: R$'))
sal = float(input('\nSalário atual: R$'))
anos = int(input('\nVocê deseja parcelar a compra em quantos anos ? \033[m'))

m = anos * 12                     # prazo em meses
pres_men = v_casa / m             # prestação mensal
salario_valido = sal * (30 / 100) # vendo quanto vale 30% do salário

if pres_men < salario_valido:
    print('\033[32m='*60)
    print('\n\033[1;32mResultado:')
    print('\nTudo certo na operação. Empréstimo concedido.\033[m')

    print(f'''\n\033[32mDados da Operacão: 
    Nome: {nome} 
    Conta: {conta} 
    Salário: R${sal:.2f} 
    Valor do Empréstimo: R${v_casa} 
    \nValor da Prestação Mensal: R$ {pres_men:.2f}''')

    print('\033[32m='*60)

else:
    print('\033[31m='*60)
    print('Seu empréstimo foi recusado, \npois a prestação mensal excederia 30% do seu salário autal.')
    print('\033[31m='*60)
