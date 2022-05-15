# from exe111.utilidadesCeV.moeda import moeda   <- a mesma coisa que importar o exe110
from exe110 import moeda
p = float(input('Digite o preço: '))
mais = float(input('Digite um aumento: '))
menos = float(input('Digite uma redução: '))
moeda.resumo_valor(p, mais, menos)
