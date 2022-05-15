#Idade para se alistar no serviço militar
import datetime

ano_nas = int(input('\nEm que você nasceu, saiba se já está pronto para o Serviço Militar: '))

ano_atual = datetime.date.today().year       # Sabendo esse ano
idade = ano_atual - ano_nas                  # Idade da pessoa

if idade == 18:
    print('\nVocê já tem 18 anos esse ano, tendo idade para se alistar no Serviço Militar.')

if idade > 18:
    dif = idade - 18
    print(f'\nVocê já tem {idade} anos, já ultrapassou {dif} anos para se alistar no Serviço Militar.'
     f' Seu alistamento foi em {ano_nas + 18}.')

if idade < 18:
    dif = 18 - idade
    print(f'\nVocê já tem {idade} anos, ainda não tem idade o suficiente para se alistar no Serviço Militar.'
          f' \nFaltam {dif} anos para você se alistar, você deve se alistar em {ano_nas + 18}.')
