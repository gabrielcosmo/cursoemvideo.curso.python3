from exe109 import moeda

p = float(input('Digite um preço: R$ '))
print('')

print(f'A metade de {moeda.moeda(p)} é {moeda.metede(p, formatar=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formatar=True)}')
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.aumentar(p, 10, formatar=True)}')
print(f'Diminuindo {moeda.moeda(p)} em 13%, temos {moeda.diminuir(p, 13, formatar=True)}')
