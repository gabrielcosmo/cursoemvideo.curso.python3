# Aumento do Salário de um trabalhador

salario = float(input('\nSalário atual: '))
aum = float(input('\nValor do aumento: '))

aum_por = aum / 100
aum_reais = aum_por * salario
salario_2 = salario + aum_reais

print(f'\nNovo Salário: R$ {salario_2:.2f} \nAumanto de: R$ {aum_reais:.2f}')
