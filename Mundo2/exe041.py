# Idade de um atleta para natação
import datetime
ano_nas = int(input('\nAno de nascimento: '))
print('')

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nas

if idade <= 9:
    print(f'Idade: {idade} \nCategoria: Mirim')

elif idade <= 14:
    print(f'Idade: {idade} \nCategoria: Infantil')

elif idade <= 19:
    print(f'Idade: {idade} \nCategoria: Júnior')

elif idade == 20:
    print(f'Idade: {idade} \nCategoria: Sênior')

elif idade > 20:
    print(f'Idade: {idade} \nCategoria: Master')
