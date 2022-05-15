# Função voto
import datetime


def voto(ano_nasc):

    idade = datetime.date.today().year - ano_nasc
    situacao = ''

    if idade < 18:
        situacao = 'Não vota'

    elif 65 > idade >= 18:
        situacao = 'Voto Obrigatório'

    else:
        situacao = 'Voto Opcional'

    return situacao


ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print('-'*40)
print(f'idade: {datetime.date.today().year - ano_nascimento} anos \nSituação eleitoral: {voto(ano_nascimento)}')
