#Conversor de Temperaturas Celsius para Fahrenheit

temp_cel = float(input('Informe a temperatura em Graus Celcius: '))

temp_fahr = temp_cel * (9/5) + 32

print(f'\nA temperatura de {temp_cel}°C equivale à {temp_fahr:.1f}F!.')