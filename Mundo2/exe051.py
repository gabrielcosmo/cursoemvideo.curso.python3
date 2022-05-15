# 10 primeiros termos de uma progressão aritmédica
import time
print('='*20, 'Conhecendo uma PA', '='*20,'\n')

p_termo = int(input('Qual o primeiro termo da PA ? '))
razao = int(input('Qual a Razão dessa PA ? '))
decimo = p_termo + (10 - 1) * razao
print('\nOs dez primeiros termos dessa PA são: ',end=' ')

for c in range(p_termo, decimo + 1, razao):
    print(f'..{c}', end=' ')
    time.sleep(0.5)
