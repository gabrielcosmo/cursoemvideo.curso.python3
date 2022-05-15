# Jogo: Adivinje o número
import random
import time

print('='*10,'Adivinhação','='*10)
n = random.randint(0,5)
jog = int(input('\nTente adivinhar em qual número estou pensando (de 0 a 5): '))

print('...')
time.sleep(2)

if jog == n:
    print(f'\033[1;32mParabéns!!! \nVocê venceu, o número certo era o número \033[0;34m{n}.')

else:
    print(f'\033[1;31mVocê perdeu. \nO número certo era o numéro \033[0;34m{n}.')

'''Cores no Terminal
Style (Estilo das letras)           Text (Cores do Texto) / Back (Cores de Fundo

0 - Padrão do Terminal              Branco   - 30           40
1 - Negrito                         Vermelho - 31           41
4 - Sublinhado                      Verde    - 32           42
7 - Inversão das cores do Texto e   Amarelo  - 33           43
    Fundo                           Azul     - 34           44
                                    Magenta  - 35           45
                                    Ciano    - 36           46
                                    Cinza    -37            47'''