# Ano Biissexto
from datetime import date

ano = int(input('\nDigite um ano e saiba se ele é Bissexto \n(digite 0 para saber sobre esse ano): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0:
    print(f'\nO ano {ano} \033[1;32mé um ano Bissexto\033[m. Portanto ele tem 366 dias.')

else:
    print(f'\nO ano {ano} \033[1;31mnão é um ano Bissexto\033[m. Portanto ele tem 365 dias.')