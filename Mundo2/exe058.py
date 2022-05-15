# Melhorando o exe028 - Jogo de adivinhação 2.0
import random
import time

contador = 1
r = 0
vit = 0
cont = 0
print('\033[32m','='*10,'Adivinhação\033[m','='*10,'\033[m')

jogador = str(input('\n\033[1;34mJogador: ')).capitalize().strip()
time.sleep(1)

print(f'\n{jogador}\033[m   vs   \033[1;31mComputador\033[m')
time.sleep(1)

lanche_jog = int(input('\nDe 1 a 5 em que número estou pensando ? '))
comp = random.randint(0, 10)


while lanche_jog != comp and r != 'n':
    r = str(input('\nVocê errou... Quer tentar de novo ? [s/n] ')).lower().strip()[0]

    while r != 's' and r != 'n':     # digitou errado o 's' ou 'n'
        r = str(input('\nVocê errou... Quer tentar de novo ? [s/n]')).lower().strip()[0]

    if r == 's':                     # continuar a jogar
        if lanche_jog > comp:
            lanche_jog = int(input(f'\nMenos que {lanche_jog}... Vamos tente de novo {jogador}! '))
        if lanche_jog < comp:
            lanche_jog = int(input(f'\nMais que {lanche_jog}... Vamos tente de novo {jogador}! '))

    if lanche_jog == comp:            # jogador acertou / contandoa vitoria
        vit += 1
    contador += 1                     # contador de tentativas

if lanche_jog == comp:                # vitoria do jogador
    print(f'\n\033[32mVocê Venceu !!! O número em que eu pensei era {comp}.')
    print(f'Tentativas: {contador}\033[m')

if lanche_jog != comp:                # derrota do jogador
    print(f'\n\033[31mVocê Perdeu... O número em que eu pensei era {comp}.')
    print(f'Tentativas: {contador}\033[m')
print('\nfim de jogo...')
