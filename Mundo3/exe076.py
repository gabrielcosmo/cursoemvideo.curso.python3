# Listagem de produtos
listagem = ('Caderno Azul', 20,
            'Caderno capa dura', 1.60,
            'Lápis', 0.50,
            'Mochila', 56,
            'Caneta', 1,
            'Tênis', 75,
            'Estojo', 5,
            'Bloco de notas', 10)

print('='*10, 'Listagem de Estoque', '='*13, '\n')

for x in range(0, len(listagem)):
                              # |
    if x % 2 == 0:            # v
        print(f'{listagem[x]:.<30}', end=' ') # lembrar da idaia dessa linha...!!
    else:
        print(f'R$ {listagem[x]:>7.2f}')
print('='*44)
