# Função várias notas


def notas(* nota, sit=False):
    """
    -> A função notas recebe várias notas de aluno e retorna um dicionário contendo:
     total de notas; maior nota; menor nota; média e situação (opcional)

    :param nota: notas de um aluno
    :param sit: caso sit=True o dicionário também contera a situacão do aluno
    :return: dicionário informando sobre a situação das notas de um aluno
    """

    dic_notas = {'total': len(nota),
                 'maior': max(nota),
                 'menor': min(nota),
                 'média': float(f'{sum(nota) / len(nota):.2f}')}

    if sit:  # situação

        if dic_notas['média'] >= 7:
            dic_notas['situação'] = 'Aprovado'

        elif 5 <= dic_notas['média'] < 7:
            dic_notas['situação'] = 'Recuperação'

        else:
            dic_notas['situação'] = 'Reprovado'

    return dic_notas


print('=-' * 50)
aluno = notas(10, 7, 8, 3.4, 8, 7, sit=True)
print(aluno)
# help(notas)
