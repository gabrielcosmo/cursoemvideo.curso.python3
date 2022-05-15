# Função Maior


def maior(* num):
    """
    -> A função maior() retorna o maior valor dentre vários valores passados.
    :param num: recebe vários números de valores indeterminados
    :return: void
    """
    n_maior = 0

    for n in num:

        if n == num[0]:
            n_maior = n

        else:
            if n > n_maior:
                n_maior = n

    print(f'O maior número foi o número {n_maior} \nOs números são: ', end=' ')
    for n in sorted(num):
        print(n, end=' ')


print('-' * 30)
maior(1, 10, 3, 4, 5, 6)
print('\n', '-' * 30)
maior(0, 4, 2, 7, 14)
print('\n', '-' * 30)
maior(5, 8, 3, 9, 0, 2, 1)
print('\n', '-' * 30)
