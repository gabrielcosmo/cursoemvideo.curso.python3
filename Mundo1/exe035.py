# Lados de um Triângulo
print('='*10,'Analisando um triângulo','='*10)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 < l2 + l3 and l1 > l2 - l3 and l1 > l3 - l2:
    print('\nCom essas medidas é possível formar um triângulo.')

elif l2 < l1 + l3 and l2 > l1 - l3 and l2 > l3 - l1:
    print('\nCom essas medidas é possível formar um triângulo.')

elif l3 < l2 + l3 and l3 > l2 - l1 and l3 > l1 - l2:
    print('\nCom essas medidas é possível formar um triângulo.')

else:
    print('\nCom esses segmentos não é possível formar um triângulo.')