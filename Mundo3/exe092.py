# Registrando uma pessoa
import datetime
registro = {}

registro['nome'] = str(input('Nome: ')).capitalize().strip()
registro['ano_nasc'] = int(input('Ano de Nascimento: '))
registro['carteira'] = int(input('Carteira de Trabalho  (caso não tenha, digite 0): '))

ano_atual = datetime.date.today().year
idade = ano_atual - registro['ano_nasc']

if registro['carteira'] != 0:
    registro['assinou_contrato'] = int(input('Ano do primeiro Contrato de Trabalho: '))
    registro['salario'] = float(input('Salário: '))

    aposentadoria = (registro['assinou_contrato'] - registro['ano_nasc']) + 35
    # soma da idade em que se assinou a carteira com mais 35 anos de contribuição

    print(f'\n\033[1mInformações do Registro de {registro["nome"]}\033[m\n')

    print(f'''Nome: {registro["nome"]}
Idade: {idade}
CTPS: {registro["carteira"]}
Ano de Contratação: {registro["assinou_contrato"]}
Salário: R$ {registro["salario"]}
Aposentadoria: {aposentadoria} anos''')

else:
    print(f'\n\033[1mInformações do Registro de {registro["nome"]}\033[m\n')

    print(f'Nome: {registro["nome"]} \nIdade: {idade} Carteira: Não tem CTPS')