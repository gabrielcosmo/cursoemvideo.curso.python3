# Sorteando uma ordem
import random
alu1 = str(input('Primeiro nome: '))
alu2 = str(input('Segundo nome: '))
alu3 = str(input('Terceiro nome: '))
alu4 = str(input('Quarto nome: '))

lista = [alu1,alu2,alu3,alu4]
random.shuffle(lista)          #random.shuffle troca as posições dos itens da lista

print(f'\nOrdem de aperesentação: {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}')
