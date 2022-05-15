def leiaInt(txt):
    """
    -> A função leiaInt recebe como parâmetro uma String como mensagem para a entrada;\n
    -> A função leiaInt lê e retorna um número inteiro, senão retorna uma mensagem de erro caso não aja
    entrada de um número inteiro.
    :param txt: Texto/Mensagem (string) passado(a) para para ser exibido antes da entrada do valor.
    :return: Int
    """

    valor_int = str(input(f'{txt}'))
    try:
        valor_int = int(valor_int)
        return valor_int

    except ValueError:
        print(f'\033[1;31mERRO! {valor_int} NÃO É UM NÚMERO INTEIRO! DIGITE UM NÚMERO INTEIRO.\033[m')

        while True:
            valor = str(input(f'{txt}'))
            if valor.isnumeric():
                return int(valor)
            else:
                print(f'\033[1;31mERRO! {valor_int} NÃO É UM NÚMERO INTEIRO! DIGITE UM NÚMERO INTEIRO.\033[m')


def leiaFloat(txt):
    """
    -> A função leiaFloat recebe como parâmetro uma String como mensagem para a entrada;\n
    -> A função leiaFloat lê e retorna um número real, senão retorna uma mensagem de erro caso não aja
    entrada de um número real.
    :param txt: Texto/Mensagem (string) passado(a) para para ser exibido antes da entrada do valor.
    :return: Float
    """

    global valor_float
    global char_var
    try:
        valor_float = str(input(f'{txt}')).replace(",", ".")
        return float(valor_float)

    except (TypeError, ValueError):
        print(f'\033[1;31mERRO! {valor_float} NÃO É UM NÚMERO INTEIRO! DIGITE UM NÚMERO INTEIRO.\033[m')

        char_var = []
        while True:
            valor = str(input(f'{txt}')).replace(",", ".")

            for c in valor:
                if c.isnumeric() or c == '.':
                    char_var.append(True)
                else:
                    char_var.append(False)

            if False in char_var or valor == '':
                print(f'\033[1;31mERRO! {valor} NÃO É UM NÚMERO INTEIRO! DIGITE UM NÚMERO INTEIRO.\033[m')
            else:
                break
            char_var.clear()

        return float(valor_float)
