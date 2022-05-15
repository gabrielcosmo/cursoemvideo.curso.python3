# Velocidade de um Carro
print('\033[1;36m='*10,'Radar Eletrônico','='*10)

vel_max = int(input('\nVelocidade máxima: '))
vel_car = float(input('\nVelocidade do carro: '))
v_km = float(input('\nPreço por Km/h acima da velocidade: \033[m '))

if vel_car > vel_max:
    dif = vel_car - vel_max
    multa = v_km * dif

    print('\033[1;31m-'*50)
    print('\nNota Oficial:')
    print(f'''\n=> O Veículo atingiu uma velocidade de {vel_car} km/h, 
    {dif} km/h a mais que o máximo permitido de {vel_max} km/h.
    Você foi multado em um valor de R${multa:.2f} .''')
    print('-'*50)

else:
    print('\033[1;32m-'*50)
    print('Nota Oficial:')
    print(f'\nO veículo atingiu uma velocidade de {vel_car} km/h \nDentro da velocidade permitida ({vel_max} km/h).')
    print('-'*50)