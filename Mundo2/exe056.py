# ANALISADOR
print('='*20,'Analisador','='*20)
soma = 0
c = 0
c2 = 0
ini_idade = 0
ini_idade2 = 0
nome_h_v = 0
nome_m_v = 0

for x in range(1,5):
    print('{:10}ª Pessoa'.format(x))
    nome = str(input('Digite seu nome: ')).title().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (m/f): ')).lower().strip()
    print('='*30)

    if sexo == 'm' and idade > ini_idade:
        ini_idade = idade
        nome_h_v = nome    # nome do homem mais velho

    if sexo == 'f' and idade > ini_idade2:
        ini_idade2 = idade
        nome_m_v = nome    # nome da mulher mais velha

    if sexo == 'm' and idade < 20:
        c += 1

    if sexo == 'f' and idade < 20:
        c2 += 1

    soma += idade

media = soma / 4
print('\n\033[1mResultado\033[m')
print(f'''\n=> Média de idade do Grupo: {media:.0f} anos
=> Nome do Homem mais velho: {nome_h_v}
=> Nome da Mulher mais velha: {nome_m_v}
=> Homens com menos de 20 anos: {c}
=> Mulheres com menos de 20 anos: {c2}''')
