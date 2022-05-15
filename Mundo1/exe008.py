# Conversor de Metros

print('-'*40)
print('Converter de Metros  para: \n1-Quilômetros \n2-Centímetros \n3-Milímetros \n')
uni = int(input())

print('-'*40)
m = float(input('Medida em Metros: '))

if uni == 1:
    km = m / (10**(3))
    print(f'{m} m equivale á: {km} km.')

if uni == 2:
    centi = m / (10**(-2))
    print(f'{m} m equivale á: {centi} cm.')

if uni == 3:
    mili = m / (10**(-3))
    print(f'{m} m equiale á: {mili} mm.')
