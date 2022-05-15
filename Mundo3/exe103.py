# Função Jogaor e gols


def print_jogador(nome, gols=''):
    """
    -> A função print_jogador() rece o nome e número de gols de um jogador
    e realiza um print das informações

    :param nome: nome do jogador
    :param gols: número de gols
    :return: void
    """
    if gols.isnumeric():
        gols = int(gols)

    else:
        gols = 0

    if nome.isalpha():      # se nome igual a vazio
        nome = '<desconhecido>'

    print('=' * 42)
    print(f'O jogador \033[3m{nome}\033[m marcou {gols} gols.')
    print('=' * 42)


print('=' * 42)
print_jogador(nome=input('Nome do jogador: ').title().strip(), gols=input('Número de gols marcados: '))
# print(print_jogador.__doc__)
