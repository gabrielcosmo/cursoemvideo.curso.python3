# Jogo de Pedra, Papel e Tesoura

import random
import time

print('\n')
print(' '*10,'\033[32;4mJogando Pedra Papel e Tesoura\033[m')

jogador = str(input('\n\033[34mJogador: \033[m')).capitalize().strip()   # Nome do Jogador
print('...')
time.sleep(1)    # Esperando 2 segundos

print(f'\n\033[34;3m{jogador}\033[m vs \033[31;3mComputador\033[m')
time.sleep(1)

lista_ppt = ['pedra','papel','tesoura']   # Lista de jogadas possíveis

print('\033[33;3m='*30)
jog_lance = str(input(f'{jogador} sua jogada é '))            # Jogada do Jogador
print('\033[33;3m=\033[m'*30)

comp = random.choice(lista_ppt)                               # Jogada do Computador
print('...')
time.sleep(1)
# Empate

if jog_lance == comp:
    print(f'\n\033[34;3m{jogador} => {jog_lance}\033[m   vs   \033[31;3m{comp} <= Computador\033[m')
    print('\033[7m Resultado: Empate \033[m')

#  Casos de vitória do Jogador

if jog_lance == 'pedra' and comp == 'tesoura' or jog_lance == 'tesoura' and comp == 'papel' or jog_lance == 'papel' and comp == 'pedra':
    print(f'\n\033[34;3m{jogador} => {jog_lance}\033[m   vs   \033[31;3m{comp} <= Computador\033[m')
    print(f'\n\033[7m Resultado: Vitória de {jogador} \033[m')

# Casos de vitória do Computador

if comp == 'pedra' and jog_lance == 'tesoura' or comp == 'tesoura' and jog_lance == 'papel' or comp == 'papel' and jog_lance == 'pedra':
    print(f'\n\033[34;3m{jogador} => {jog_lance}\033[m   vs   \033[31;3m{comp} <= Computador\033[m')
    print(f'\n\033[7m Resultado: Vitória do Computador \033[m')

# Caso do jogador não escolher pedra,papel ou tesoura

if jog_lance != 'pedra' and jog_lance != 'tesoura' and jog_lance != 'papel':
    print(f'\033[7mResultado: {jogador} não jogou pedra, papel ou tesoura.\033[m '
          f'\n\033[7mEntão a vitória é do Computador.\033[m')
