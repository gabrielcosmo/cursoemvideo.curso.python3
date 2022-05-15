#Ângulo: Senno, Cosseno e Tangente
import math

ang = float(input('Madida do ângulo: '))

seno = math.sin(math.radians(ang))           #Primeiro converter para Radianos 
cosseno = math.cos(math.radians(ang))
tangente = math.tan((math.radians(ang)))

print(f'\nSeno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
