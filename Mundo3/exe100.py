# Função Sorteando e somando números
import time, random


def sortear():
    """
    -> A função sortear() retorna uma lista de cinco valores aleatórios.
    :return: valor do tipo list(), contendo cinco valores aleatórios.
    """
    lista_sorteio = [
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10),
        random.randint(0, 10)]
    return lista_sorteio


def somaPar(lst):
    """
    -> A função somaPar() retorna a soma de todos os valores pares de uma lista.
    :param lst: valor do tipo list() recebida.
    :return: a soma de todos os números pares.
    """
    s = 0
    for n in lst:

        if n % 2 == 0:
            s += n
    return s


seq = int(input('Número de sorteios: '))

for x in range(0, seq):
    print('-' * 40)
    lista = sortear()
    soma_ = somaPar(lista)
    print(f'Os números sorteados foram: ', end=' ')

    for n in lista:
        print(n, end=' ')
    print(f'\nA soma entre os números pares é igual a {soma_}.')
    time.sleep(0.5)
    print('-' * 40)
