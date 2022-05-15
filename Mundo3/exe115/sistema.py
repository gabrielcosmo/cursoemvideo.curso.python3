from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo('cursoemvideo.txt')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # ler conteúdo do arquivo.
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')

        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq=arq, nome=nome, idade=idade)

    elif resposta == 3:
        # Opção de sair do Sistema.
        cabeçalho('Saindo do Sistema...')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[1;31mERRO: Digite um número válido.\033[m')
    sleep(2)
