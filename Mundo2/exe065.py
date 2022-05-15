# Menor, Maior e Média entre vários valores
n = res = 0
soma = num_n = 0
menor = maior = media = 0
n_lista = []
x = 0
print('='*10,'Lendo vários Valores','='*10)

while res != 'n':
    n = int(input('\nDigite um número: '))
    soma += n
    res = str(input('\nVocê quer continuar a digitar ? [s/n] ')).lower().strip()[0]

    while res != 's' and res != 'n':
        res = str(input('\nVocê quer continuar a digitar ? [s/n] ')).lower().strip()[0]

    if n > maior:
        maior = n

    n_lista.append(n)
    num_n += 1

menor = maior
while x < len(n_lista):

    if n_lista[x] < menor:
        menor = n_lista[x]
    x += 1

media = soma / num_n

print('-'*40)
print(f'''Soma entre todos os números: {soma}
Maior valor: {maior}
Menor valor: {menor}
Média dos valor: {media:.2f}''')
