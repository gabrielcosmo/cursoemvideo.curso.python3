# Função print adaptável


def titulo_adap(txt, traco='-'):
    """
    -> A função titulo_adap realiza um print entre linhas de tamanho ajustável ao texto.
    :param txt: texto para a exibição.
    :param traco: tracezados entre os quais fica o texto, é variável (default = '-').
    :return: void
    """
    print(f'{traco}' * len(txt))
    print(f'{txt:^}')
    print(f'{traco}' * len(txt))


# Programa Principal
titulo_adap(' JavaScript ')
titulo_adap(' Python ')
titulo_adap('Aprendendo funcões em Python')
titulo_adap('   JAVA   ', '=')
