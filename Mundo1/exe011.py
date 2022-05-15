#Quantidade de tinta para uma pintar uma a área de uma parede

lar = float(input('\nLargura da parede: '))
print('-'*30)
alt = float(input('Alatura da parede: '))
print('-'*30)
area_t = float(input('Área coberta por um litro de tinta: '))
print('-'*30)

area_p = lar * alt
q_tinta = area_p / area_t

print(f'Serão necessários {q_tinta:.2f} litros para pintar uma área de {area_p:.2f} m² ({lar}x{alt}).')