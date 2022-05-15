from exe108 import moeda
p = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metede(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo {moeda.moeda(p)} em 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
