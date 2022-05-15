# Função calculo de fatorial


def fatorial(num, show=False):
    """
    -> a função fatorial() calcula o fatorial de número num

    :param num: número
    :param show: exibir calculo
    :return: fatorial de num
    """
    cal = []
    f = 1

    for x in range(num, 0, -1):
        f *= x

    if not show:  # se show == False
        return f

    else:

        for x in range(num, 0, -1):
            cal.append(f'{x}')
        return f'{" x ".join(cal)} = {f}'


n = int(input('Digite um úmero e veja seu fatorial: '))
print('-='*30)
print(fatorial(n, show=True))
print('-='*30)
