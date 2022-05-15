# Aproveitamento de um Jogador V2.0

print(f'\n{"-Análise de Desempengo Jogadores-":%^50}\n')
dic_jog = {}
lista_todos = []
gols = []
total = res = 0
maior = x = jog = apro = apro2 = 0

while True:

    gols = []
    total = 0
    dic_jog['nome'] = str(input('Nome: ')).title().strip()   # nome
    num_jogs = int(input(f'Número de jogos disputados por {dic_jog["nome"]}: '))  # número de jogos
    print('-'*50)

    for x in range(1, num_jogs+1):  # Obtendo os gols/partida
        variavel_gol = int(input(f'Número de Gols na {x}º partida: '))
        total += variavel_gol
        gols.append(variavel_gol)

    dic_jog['gols'] = gols[:]    # dic_jog recebe a cópia dos gols
    dic_jog['total'] = total     # recebe total de gols
    lista_todos.append(dic_jog.copy())  # lista_todos recebe a cópia do dicionário do registro
    print('-'*50)

    res = str(input('Deseja registrar mais um Jogador? ')).lower().strip()[0]  # continuar ?

    while res != 's' and res != 'n':
        res = str(input('Deseja registrar mais um Jogador? '))
    print('-'*30)

    if res == 'n':    # Break / Exibir resultados

        print(f'{"-Aproveitamento-":%^50}\n')
        print(f'{"Jogador":<20}', f'{"Gols":<10}', f'{"Total":>10}\n')

        for apro in lista_todos:   # Exibir Registro: nome

            for apro2 in lista_todos:
                # Ajuste do quadro de exibição: preenchimento dos espaços com '-' e alinhamento

                if len(apro2['gols']) > maior:
                    maior = len(apro2['gols'])

                while len(apro2['gols']) < maior:  # preenchendo com '-'
                    apro2['gols'].append('-')

            print(f'{lista_todos.index(apro)+1}º {apro["nome"]:.<20}', end=' ')

            for x in apro["gols"]:  # Exibir Registro: gols
                print(f'{x}', end=' ')

            print(f'{apro["total"]:.>10}')  # total de gols

        print('-'*50)
        res = str(input('Deseja conferir os utilidadesCeV de um jogador especfíco ? ')).lower().strip()[0]

        while res != 's' and res != 'n':
            res = str(input('Deseja conferir os utilidadesCeV de um jogador especfíco ? '))
        print('-' * 50)

        while res == 's':
            jog = int(input('Digite o número do jogador que você ver os utilidadesCeV: '))

            print(f'\n{lista_todos[jog - 1]["nome"]:.<20}', end='')

            for x in lista_todos[jog-1]['gols']:
                print(x, end=' ')
            print(end='  ')
            print(lista_todos[jog-1]["total"])
            print('-'*50)

            res = str(input('Deseja conferir os utilidadesCeV de um jogador especfíco ? '))
        break
