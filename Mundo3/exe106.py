# Função para Interactiv Help


def acesso_docstrings(fun_bibl):
    help(fun_bibl)


print(f'\033[1;31m{"=" * 60}\033[m')
print(f'\033[1;31m{" Sistema Interativo de ajuda ":=^60}\033[m')
print(f'\033[1;31m{"=" * 60}\033[m')
print('')
while True:

    fun = input('\033[1;32mNome da função ou biblioteca: \033[m')
    print('-=' * 40)
    print(f'\033[34m')
    acesso_docstrings(fun)
    print('\033[m')
    print('-=' * 40)

    resp = input('\033[1;37mVocê deseja continuar [sim/não] ? \033[m').strip().lower()[0]

    while resp != 's' and resp != 'n':
        resp = input('\033[1;37mVocê deseja continuar [sim/não] ? \033[m').strip().lower()[0]

    if resp == 'n':
        break
    print('-=' * 40)
