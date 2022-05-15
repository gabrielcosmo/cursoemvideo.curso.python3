# Aproveitamento de um Jogador

jogador = {}
gols = []
s = 0
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
jogador['partidas'] = int(input(f'Números de partidas disputadas por {jogador["nome"]}: '))
print('')

for g in range(1, jogador['partidas'] + 1):
    gols.append(int(input(f'Números de gols na {g}º partida: ')))
    jogador['gols por jogo'] = gols[:]

for n in jogador['gols por jogo']:
    s += n

jogador['total'] = s

print(f'\n{"Aprveitamento":=^33}')

print(f'Nome: {jogador["nome"]}\n')

print('Gols por partida:')
for x in range(0,len(jogador['gols por jogo'])):
    print(f'  {x + 1}º partida: {jogador["gols por jogo"][x]}')

print('')
print(f'Total de Gols: {jogador["total"]}')
print(f'Média de Gols/jogo: {jogador["total"]/jogador["partidas"]} gols')