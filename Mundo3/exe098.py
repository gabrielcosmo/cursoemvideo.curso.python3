# Função Contagem personalizada


def contagem(inicio, fim, passo=1):
    """
    -> A função contegem() realiza uma contagem,
    de um número de inicio (inicio) a um número de parada (fim)
    fazendo um passo (passo).

    :param inicio: número de inicio da contagem.
    :param fim: número do fim da contagem.
    :param passo: número referente ao passo da contegem (default = 1)
    (ex.: inicio, inicio + passo, ...,fim)
    :return: void
    """
    import time

    if passo < 0:
        passo *= -1

    if inicio < fim:
        for n in range(inicio, fim, passo):
            print(n, end=' ')
            time.sleep(0.2)

    else:
        for n in range(inicio, fim, -passo):
            print(n, end=' ')
            time.sleep(0.2)


print(f'{" Sequência Personalizada ":=^40}')
contagem(10, 1)
print('')
contagem(10, 0, 2)

ini = int(input('\n\nDigite um número para o inicio: '))
print('-' * 30)

fim = int(input('Digite um número para o fim: '))
print('-' * 30)

pas = int(input('Digite um numero para o passo: '))
print('-' * 30)
contagem(ini, fim, pas)
