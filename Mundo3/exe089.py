# Boletim escolar

lista_registro = []
lista_aluno = []
lista_notas = []
palavras = [' Boletim ', 'Aluno', 'Nota 1', 'Nota 2', 'Média', ' Registro Acadêmico ']
print(f'\033[1m{palavras[5]:=^60}\033[m')
while True:

    if len(lista_aluno) == 0:
        lista_aluno.append(str(input('\nDigite o nome do aluno: ')).strip().title())  # nome do aluno
        lista_notas.append(float(input('Digite a sua primeira nota: ')))              # primeira nota
        lista_notas.append(float(input('Digite a sua segunda nota: ')))               # segunda nota
        lista_notas.append((lista_notas[0] + lista_notas[1]) / 2)                     # média
        lista_aluno.append(lista_notas[:])                          # colocando a cópia da lista_notas em lista_aluno
        lista_registro.append(lista_aluno[:])                       # colocando a cópia da lista_aluno em lista_registro

    else:
        lista_aluno[0] = str(input('\nDigite o nome do aluno: ')).strip().title()
        lista_notas[0] = float(input('Digite a sua primeira nota: '))
        lista_notas[1] = float(input('Digite a sua primeira nota: '))
        lista_notas[2] = (lista_notas[0] + lista_notas[1]) / 2
        lista_aluno[1] = lista_notas[:]
        lista_registro.append(lista_aluno[:])

    res = str(input('\nContinuar ? [sim/não] ')).strip().lower()[0]  # continuar...
    while res not in 'sn':
        res = str(input('\nContinuar ? [sim/não] ')).strip()[0]
    print('-'*60)
    if res == 'n':
        break

print('\n', f'\033[1m{palavras[0]:=^60}') # exibição do boletim geral
print(f'{palavras[1]:-^30} {palavras[2]} {palavras[3]} {palavras[4]}\033[m')

for boletim in range(0,len(lista_registro)):  # mostrando as notas e médias

    print(f'\033[1m{lista_registro[boletim][0]:.<30}\033[1m ', end=' ')

    for notas in lista_registro[boletim][1]:
        print(f'\033[1m{notas}\033[m ', end=' ')
    print('')

print('-'*60)
while True:   # mostrando as notas de um aluno
    res = str(input('\nVocê deseja ver as notas de algum aluno ? [sim/não] ')).strip().lower()[0]

    while res not in 'sn':
        res = str(input('\nVocê deseja ver as notas de algum aluno ? [sim/não] ')).strip().lower()[0]

    if res == 's':
        aluno = str(input('Nome do aluno: ')).strip().title()

        for d in range(0, len(lista_registro)):

            if aluno in lista_registro[d][0]:
                print(f'{aluno:.<30}', end=' ')
                for notas in lista_registro[d][1]:
                    print(f'{notas}', end=' ')
        print('')
    if res == 'n':
        break
