# Tabela do Brasileirão
import time
print('='*10, 'Tabela do Brasileirão 2019','='*10)

tabela_2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
               'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceára',
               'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

# Lista em ordem alfabética

print('\033[1;36mTimes do Brasileirão 2019:\n\033[m')
for x in sorted(tabela_2019):      # o sorted() não altera a tupla, apenas exibe em ordem alfabética
    print(f'\033[1;36m{x}\033[m')
print('='*50)

# 5 primeiros colocados

print('\033[1;33mOs 5 primeiros colocados são:\033[m')

for col in range(0, 6):
    print(f'\033[32m{col + 1:2}º {tabela_2019[col]}\033[m')
print('='*50)

# 4 últimos colocados
print('\033[1;32mOs últimos 4 colocados são:\033[m')

for col in range(16, 20):
    print(f'\033[31m{col + 1:2}º {tabela_2019[col]}\033[m')
print('='*50, '\n')

# Ver seu time na tabela

seu_time = str(input('Confira a posição do seu time na classificação [digite o nome dele]: ')).title().strip()

while seu_time not in tabela_2019:
    print('Ele não está entre os 20 times do campeonato. Tente de novo.\n')
    seu_time = str(input('Confira a posição do seu time na classificação [digite o nome dele]: '))

time.sleep(0.5)
print(f'\nO {seu_time} está na {tabela_2019.index(seu_time) + 1}º posição no campeonato.')
time.sleep(2)

# Ver tabela Completa

ver_tabela = str(input('\nVocê deseja ver a tabela completa ? [sim/não] ')).strip()[0]

while ver_tabela not in 'SsNn':
    ver_tabela = str(input('\nVocê deseja ver a tabela completa ? [sim/não] ')).strip()[0]

if ver_tabela in 'Ss':

    # Tabela completa
    print('\033[1;32m', '='*10, 'Tabela Completa 2019', '='*10, '\033[m', '\n')
    for col in range(0,len(tabela_2019)):
        if col < 6:
            print(f'\033[32m{col + 1:2}º {tabela_2019[col]}\033[m')

        elif 5 < col <= 7:
            print(f'\033[34m{col + 1:2}º {tabela_2019[col]}\033[m')

        elif 7 < col <= 15:
            print(f'\033[36m{col + 1:2}º {tabela_2019[col]}\033[m')

        else:
            print(f'\033[31m{col + 1:2}º {tabela_2019[col]}\033[m')
        time.sleep(0.1)
    print('='*50)
