# Maior e Menor número

n1 = float(input('\nDigite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

if n1 > n2 > n3:
    print(f'\nMaior: {n1} \nMenor{n3} \n=> {n3}, {n2}, {n1}')

if n1 > n3 > n2:
    print(f'\nMaior: {n1} \nMenor: {n2} \n=> {n2}, {n3}, {n1}')

if n2 > n1 > n3:
    print(f'\nMaior: {n2} \nMenor: {n3} \n=> {n3}, {n1}, {n2}')

if n2 > n3 > n1:
    print(f'\nMaior: {n2} \nMenor: {n1} \n=> {n1}, {n3}, {n2}')

if n3 > n2 > n1:
    print(f'\nMaior: {n3} \nMenor: {n1} \n=> {n1}, {n2}, {n3}')

if n3 > n1 > n2:
    print(f'\nMaior: {n3} \nMenor: {n2} \n=> {n3}, {n1}, {n2}')