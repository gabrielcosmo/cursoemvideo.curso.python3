# Modulo Moeda.py p/ o teste107.py


def aumentar(preco, aumento, formatar=False):
    pre_com_aumento = preco + (preco * (aumento / 100))

    if formatar:
        return moeda(pre_com_aumento)

    else:
        return pre_com_aumento


def diminuir(preco, reducao, formatar=False):
    pre_com_reducao = preco - (preco * (reducao / 100))

    if formatar:
        return moeda(pre_com_reducao)

    else:
        return pre_com_reducao


def dobro(preco, formatar=False):
    pre_dobro = preco * 2

    if formatar:
        return moeda(pre_dobro)

    else:
        return pre_dobro


def metede(preco, formatar=False):
    metade_pre = preco / 2

    if formatar:
        return moeda(metade_pre)

    else:
        return metade_pre


def moeda(valor):
    """
    -> A função moeda() retorna um valor monetário formatado.
    :param valor: valor a ser formatado
    :return: valor (string) formatado
    """
    return f"R$ {valor:.2f}".replace('.', ',')
