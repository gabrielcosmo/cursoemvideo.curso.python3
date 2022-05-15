# Analisando a resposta do Usuário
s = 0
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo (M/F): ')).upper().strip()[0]
print('\nRegistro feito.\nFim do programa.')
