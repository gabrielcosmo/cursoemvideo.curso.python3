#Sortear um aluno
import random

alu1 = str(input('\nNome do aluno: '))
alu2 = str(input('Nome do segundo aluno: '))
alu3 = str(input('Nome do terceiro aluno: '))
alu4 = str(input('Nome do quarto aluno: '))

lista = [alu1,alu2,alu3,alu4]
escolhido = random.choice(lista)       #random.choice escolhe um item de lista aleatório

print(f'\nO aluno esolhido foi {escolhido}.')
