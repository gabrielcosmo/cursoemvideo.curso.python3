# Maioridade
import datetime
maior = 0
menor = 0
idade = 0

for p in range(1, 8):
    ano_nas = int(input(f'\nDigite a data de nascimento da {p}ª pessoa: '))
    idade = datetime.date.today().year - ano_nas

    if idade >= 21:
        maior += 1

    if idade < 21:
        menor += 1
print('='*45)
print(f'\nPessoas com Maioridade: {maior} \nPessoas que não tem maioridade ainda: {menor}')
