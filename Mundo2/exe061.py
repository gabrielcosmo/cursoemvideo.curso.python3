# Refazendo o exe051 - Progressão Aritmédica
import time
print('='*10,'Progressão Aritmédica v2.0','='*10)
p_termo = int(input('\nDigite o primeiro termo termo dessa PA: '))
razao = int(input('Digite a razão dessa PA: '))
decimo = p_termo
x = 1

print(f'\nOs dez primeiros termos dessa PA são: {p_termo}',end=' ')

while x < 10:
   p_termo = decimo + razao
   decimo = p_termo
   x += 1
   time.sleep(0.5)
   print(decimo,end=' ')