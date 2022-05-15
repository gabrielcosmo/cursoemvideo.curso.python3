# Modulo Moeda.py p/ o teste107.py


def aumentar(preco, aumento):
    pre_com_aumento = preco + (preco * (aumento / 100))
    return pre_com_aumento


def diminuir(preco, reducao):
    pre_com_reducao = preco - (preco * (reducao / 100))
    return pre_com_reducao


def dobro(preco):
    pre_dobro = preco * 2
    return pre_dobro


def metede(preco):
    metade_pre = preco / 2
    return metade_pre


def moeda(valor):
    return f"R$ {valor}".replace('.', ',')
