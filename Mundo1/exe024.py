# Sabendo se o nome de uma cidade tem tal nome

cidade = str(input('\nNome da Cidade: ')).strip()
nome1 = str(input('O nome procurado é ')).strip()

cidade2 = cidade.lower()
nome2 = nome1.lower()
cidade_div = cidade2.split()

res = nome2 in cidade_div[0]
print(f'\nO nome {cidade} apresenta como primeiro nome a palavra {nome1}? {res}.')