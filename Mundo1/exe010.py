#Converter Reais par Dólares

valor_r = float(input('Quantos reais voçê  tem ? R$ '))
valor_d = float(input('Qual acotação atual do Dólar ? R$ '))

res = valor_r / valor_d

print(f'\nAtualmente voçê tem US${res:.2f} (dolares).')
