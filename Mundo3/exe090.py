#Situação de um aluno

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

print('')
if aluno['media'] >= 7:
    print(f'Nome: {aluno["nome"]} \nMédia: {aluno["media"]}. \nSitução: Aprovado(a).')
    aluno['situacao'] = 'aprovado'

elif 5 <= aluno['media'] < 7:
    print(f'Nome: {aluno["nome"]} \nMédia: {aluno["media"]}. \nSitução: Recuperação.')
    aluno['situacao'] = 'recuperação'

else:
    print(f'Nome: {aluno["nome"]} \nMédia: {aluno["media"]}. \nSitução: Reprovado(a).')
    aluno['situacao'] = 'reprovado'