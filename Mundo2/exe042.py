# Lados de um Triângulo e seu tipo

print('\n','='*10,'Analisando um triângulo','='*10)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
teste = 0
print('-'*50)

# Testando se é um triânngulo
if (l1 < l2 + l3) and (l1 > l2 - l3) and (l1 > l3 - l2):
    print('\nCom essas medidas é possível formar um triângulo.')
    teste += 1

elif (l2 < l1 + l3) and (l2 > l1 - l3) and l2 > (l3 - l1):
    print('\nCom essas medidas é possível formar um triângulo.')
    teste += 1

elif (l3 < l2 + l3) and (l3 > l2 - l1) and (l3 > l1 - l2):
    print('\nCom essas medidas é possível formar um triângulo.')
    teste += 1
# ...até aqui

# Sabendo qual o tipo do triângulo
if teste == 1:
    if l1 == l2 == l3:
        print('Esse é um triângulo Equilátero.')

    if l1 == l2 and l1 != l3:
        print('Esse é um triângulo Isóceles.')

    if l1 == l3 and l1 != l2:
        print('Esse é um triângulo Isóceles.')

    if l2 == l3 and l2 != l1:
        print('Esse é um triângulo Isóceles.')

    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Esse é um triângulo Escaleno.')

#Não é um Triângulo
else:
    print('\nCom esses segmentos não é possível formar um triângulo.')
print('-'*50)
