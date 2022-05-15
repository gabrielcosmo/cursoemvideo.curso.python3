# Cadastrando várias pessoas / unindo dicionários e listas

lista_todas = []
pessoa = {}
n_mulh = soma = 0
acima_media = []
while True:

    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    pessoa['sexo'] = str(input('Sexo: ')).capitalize().strip()[0]

    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':    # teste se sexo é 'M' ou 'F'
        pessoa['sexo'] = str(input('Sexo: ')).capitalize().strip()[0]

    pessoa['idade'] = int(input('Idade: '))

    lista_todas.append(pessoa.copy())

    print('='*30)
    res = str(input('Quer continuar [sim/não]? ')).strip().lower()[0]

    while res != 's' and res != 'n':
        res = str(input('Quer continuar [sim/não]? ')).strip().lower()[0]

    print('='*30)

    if res == 'n':  # interromper laço
        break

n_pessoa = len(lista_todas)

for n in lista_todas:

    if n['sexo'] == 'F':  # contagem do números de mulheres
        n_mulh += 1

    soma += n['idade']  # soma das idades

media = soma / n_pessoa # média das idades

for dic in lista_todas:

    if dic['idade'] > media:
        acima_media.append(dic.copy())

print(f'Número de Pessoas: {n_pessoa}')
print(f'Média de idade das pessoas: {media:.1f}')
print(f'Mulheres cadastradas: {n_mulh}\n')
print('Pessoas acima da média:')
print('-'*23)
for p in acima_media:
    print(f'Nome: {p["nome"]}', end=' ')
    print(f'Sexo: {p["sexo"]}', end=' ')
    print(f'Idade: {p["idade"]}')