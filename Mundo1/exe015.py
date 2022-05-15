#Carros alugados

km = float(input('Quantidade de quilômetros rodados: '))    #O Km rodado custa R$ 0,15
dias = int(input('Quantidade de dias rodados: '))           #O dia custa R$ 60,00

valor_km = km * 0.15
valor_dia = dias * 60
total = valor_dia + valor_km

print('\nO total a pagar é de R$ {}.'.format(total))
print('\n-> Valor a pagar por Km rodado: R$ {:.2f} \n-> Valor a pagar pelos dias: R$ {:.2f}'.format(valor_km,valor_dia))
