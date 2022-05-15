# Identificando Vogais em várias palavras

tupla_palavras = ('Futebol', 'Brasil', 'Tecnico', 'Informatica', 'Instituto Federal', 'Filme', 'Pesquisa', 'Cientifico',
                  'Estudo','Python', 'Chanpions League', 'Libertadores', 'Infinito', 'Matematica') # sem acentos
vogal = ('a', 'e', 'i', 'o', 'u')

for palavra in tupla_palavras:
    print(f'No termo \033[1m{palavra.upper()}\033[m temos as vogais:', end=' ')

    for letra in vogal:

        if letra in palavra:
            print(f'\033[1m{letra}', end=' ')

    print('\n')
    print('-' * 50)
