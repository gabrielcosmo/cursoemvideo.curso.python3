# Função leiaint()


def leiaInt(txt):
    """
    -> A função leiaInt() recebe um texto para ser exibido como mensagem
       e só aceita, e retorna, um número inteiro; senão exibe ema mensagem de erro

    :param txt: mensagem a ser exibida pelo leiaInt()
    :return: inteiro n
    """
    ok = False
    valor = 0

    while True:
        n = input(f'{txt}')

        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

        if ok:
            break
    return valor


# Programa Principal
num = leiaInt('Digite um número: ')
print('=-' * 30)
print(f'O número inteiro ditado foi {num}')
# help(leiaInt)
