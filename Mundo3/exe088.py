# Sortiando Jogos
import random
import time
lista_todos_jogos = []
lista_jogos = []
n_jogos = int(input('\nVocê quer sortiar quantos jogos ? '))

for sorteio in range(0, n_jogos):

    for num in range(0, 6):
        num_sort = random.randint(1, 60)

        while num_sort in lista_jogos:
            num_sort = random.randint(1, 60)

        lista_jogos.append(num_sort)

    lista_todos_jogos.append(lista_jogos[:])
    lista_jogos.clear()

a = f' Números dos {n_jogos} jogos '
print(f'\n{a:=^50}\n')

for num in range(0,len(lista_todos_jogos)):
    print(f'{num + 1}º jogo: ', end=' ')

    for num2 in lista_todos_jogos[num]:
        print(f'{num2}', end=' ')
    time.sleep(0.5)
    print('')