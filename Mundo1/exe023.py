#Unidades de um número
print('=======Casas Decimais de um Número======')

n = int(input('Digite um número entre 0 e 9999: '))

u = (n // 1) % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

print(f'\nMilhar: {m} \nCentena: {c} \nDezena: {d} \nUnidade: {u}')