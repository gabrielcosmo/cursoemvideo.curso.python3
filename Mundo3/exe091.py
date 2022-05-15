#Jogo de Dados
import random
import time
jogo = {}
lista_jog = [0, 0, 0, 0]

print(f'\033[1m{"Jogo de Dados":-^30}')

for j in range(0, 4):
    lista_jog[j] = random.randint(1, 6)

lista_jog.sort(reverse=True)

for j in range(0, len(lista_jog)):
    n = j+1
    jogo['jogador '+str(n)] = lista_jog[j]

print('\nRanking dos Jogadores:\n')
print(f'{"Jogador":>8}{"Número":>18}\n')

for k, v in jogo.items():

    if k == 'jogador 1':
        print(f'{k:.<20} {v} (Vencedor)')
        time.sleep(0.5)
    else:
        print(f'{k:.<20} {v}')
        time.sleep(0.5)