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

mais_termos = str(input('\nVocê quer ver mais termos dessa PA ? [s/n] ')).lower()

while mais_termos != 's' and mais_termos != 'n':
    mais_termos = str(input('\nVocê quer ver mais termos dessa PA ? [s/n] ')).lower()

if mais_termos == 's':
    mais_termos = int(input('\nDigite quantos termos a mais quer ver: '))
    x = 0
    while x < mais_termos:
        p_termo = decimo + razao
        decimo = p_termo
        print(decimo,end=' ')
        time.sleep(0.5)
        x += 1
