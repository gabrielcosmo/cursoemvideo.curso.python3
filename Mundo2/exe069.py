# Registrando vários utilidadesCeV
cont_maior = 0
cont_homens = 0
cont_mul_menos_vinte = 0

print('='*10,'Cadastro','='*10)
while True:
    print('\n','='*20)
    nome = str(input('\nDigite seu nome: ')).strip()
    idade = int(input('\nDigite sua idade: '))
    sexo = str(input('\nDigite seu sexo [M/F]: ')).strip()

    while sexo not in 'MmFf':
        sexo = str(input('\nDigite seu sexo [M/F]: ')).strip()

    if idade > 18:
        cont_maior += 1

    if sexo in 'Mm':
        cont_homens += 1

    if sexo in 'Ff' and idade < 20:
        cont_mul_menos_vinte += 1

    continuar = str(input('\nContinuar [s/n]: ')).lower().strip()[0]

    while continuar not in 'SsNn':
        continuar = str(input('\nContinuar [s/n]: ')).lower().strip()[0]

    if continuar == 'n':
        break
print('\n', '='*20)
print(f'''\nPessoas com mais de 18 anos: {cont_maior}
Número de Homens: {cont_homens}
Número de Mulheres com menos de 20 anos: {cont_mul_menos_vinte}''')
