def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\n\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(lin='-', tam=25):
    return lin * tam


def cabeçalho(txt):
    print('')
    print(f'{linha("=")} {txt} {linha("=")}')
    print('')


def menu(lista):
    cabeçalho('MENU PRINCIPAL')

    for c, item in enumerate(lista):
        print(f'\033[33m{c + 1}\033[m >> \033[34m{item}\033[m')
    print(linha())

    opc = leiaInt('\033[32mDigite a opção desejada: \033[m')
    return opc
