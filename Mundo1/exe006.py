# Dobro, Triplo  e Raiz quadrada de um número

print('='*40)
print('Veja: \n-O dobro \n-O triplo \n-A raiz quadrada')

print('='*40)
n = int(input('Digite um número: '))
print('='*40)

d = n * 2
t = n * 3
r = n ** (1/2)

print(f'Dobro: {d} \nTriplo: {t} \nRaiz Quadrada: {r:.2f}')
