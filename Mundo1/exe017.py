#Catetos e Hipotenusa
import math

cat_ad = float(input('Medida do cateto adjacente: '))
cat_op = float(input('\nMedida do cateto oposto: '))

h = math.sqrt(cat_op**2 + cat_ad**2)
print(f'\nHipotenusa: {h:.2f}')

