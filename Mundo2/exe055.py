# Maior e Menor peso
maior = 0
menor = 0
lista_peso = []
print('')
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: Kg '))
    lista_peso.append(peso)

    if peso > maior:
        maior = peso

menor = maior

for m in lista_peso:

    if m < menor:
        menor = m

print(f'\nMaior peso: {maior} Kg \nMenor peso: {menor} Kg')
