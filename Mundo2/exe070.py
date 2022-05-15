# Loja
pre = nome_pro = 0
valor_compra = nome_pro_barato = 0
cont = menor = 0

print('='*10,'Lojas','='*10,'\n')
while True:
    print('-' * 30)
    nome_pro = str(input('\nNome do produto: '))
    pre = int(input(f'\nPreço do produto ({nome_pro}): R$ '))
    valor_compra += pre
    cont += 1       # contador de produtos
    if cont == 1:   # o primeiro produto é mais barato
        menor = pre
        nome_pro_barato = nome_pro
    else:                # se tiver mais de um produto haverá o teste
        if pre < menor:  # se preço menor que o menor - que era o primeiro - o menor passa a ser ele
            menor = pre
            nome_pro_barato = nome_pro

    if pre > 1000:
        cont += 1

    continuar = str(input('\nDeseja continuar: [s/n] ')).lower().strip()[0]

    while continuar not in 'sn':
        continuar = str(input('\nDeseja continuar: [s/n] ')).lower().strip()[0]

    if continuar == 'n':
        break

print('\n', '='*30)
print(f'''Valor Total na compra: R$ {valor_compra}
Produtos acima de R$ 1000: {cont}
Produto de menor valor: {nome_pro_barato} (R$ {menor})''')
