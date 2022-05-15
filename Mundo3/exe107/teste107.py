from exe107 import moeda

p = float(input('Digite um preço: R$ '))
print('=' * 30)
print(f'A etade de R$ {p} é R$ {moeda.metede(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando R$ {p} em 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuindo R$ {p} em 13%, temos R$ {moeda.diminuir(p, 13)}')
