#IMC de uma pessoa

print('='*15,'Calculadora de IMC','='*15)

massa = float(input('\nDigite seu peso: (kg) '))
altura = float(input('\nDigite sua altura: '))
imc = massa / (altura**2)
print('-'*50)

if imc < 18.5:
    print(f'Imc: {imc:.2f} \n\033[7mStatus: Abaixo do peso\033[m')

if 18.5 <= imc < 25:
    print(f'Imc: {imc:.2f} \n\033[7mStatus: Peso ideal\033[m')

if 25 <= imc < 30:
    print(f'Imc: {imc:.2f} \n\033[7mStatus: Sobrepeso\033[m')

if 30 <= imc < 40:
    print(f'imc: {imc:.2f} \n\033[7mStatus: Obesidade\033[m')

if imc > 40:
    print(f'Imc: {imc:.2f} \n\033[7mStatus: Obesidade mórbida\033[m')
