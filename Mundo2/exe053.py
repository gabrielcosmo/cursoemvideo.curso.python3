# Lendo um Políndromo
print('='*20,'Lendo um Palíndromo','='*20)

frase = str(input('\nDigite uma frase e saiba se ela é um palíndromo: '))

frase2 = frase.lower().split()         # Frase com letras minúsculas e colocada em forma de lista
frase3 = ''.join(frase2)               # Frase junta sem os espaços
frase_contra = []                      # Lista para receber a frase ao contrário

for x in range(len(frase3)-1,-1,-1):   # Inversão da frase
    frase_contra.append(frase3[x])

frase_contra2 = ''.join(frase_contra)   # Juntando a frase ao contrário

if frase_contra2 == frase3:
    print(f'\nEssa frase é um Palímdromo, pois pode ser lida ao contrário com mesmo sentido. '
          f'\n\nFrase: {frase3} \nFrase ao Contrário: {frase_contra2}')

else:
    print('\nEssa frase não é um palímdromo.')
# Apenas uma linha em vez do for => print(frase3[::-1])
