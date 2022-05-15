# Anaisando uma expressão com parênteses
frase_print = ' Analisador de expressões '
print(f'{frase_print:=^60}')

expre = str(input('\nDigite uma expressão: ')).strip()
lista_parenteses = []

for simb in expre:
    if simb == '(':
        lista_parenteses.append('(')

    elif simb == ')':

        if len(lista_parenteses) > 0:
            lista_parenteses.pop() # elimina o último
        else:
            lista_parenteses.append(')')

if len(lista_parenteses) == 0:
    print(f'\nA expressão {expre} é válida.')
else:
    print(f'\nA expressão {expre} não é válida.')
