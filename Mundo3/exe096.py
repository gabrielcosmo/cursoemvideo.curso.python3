# Funções Área de um terreno


def area(largura, comprimento):
    """
    -> A função area() calcula a área a partir da largura e comprimento
    :param largura: largura do terreno
    :param comprimento: comprimento do terreno
    :return: void
    """
    ar = largura * comprimento
    print(f'A área do terreno é de {ar} m².')


# Programa Principal
lar = float(input('Largura do terreno: '))
comp = float(input('Comprimento do terreno: '))
print('-'*20)
area(lar, comp)
