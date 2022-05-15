from exe115.lib.arquivo import *
from exe115.lib.interface import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        # 'rt' -> r: read (ler) t: text (texto)
        a.close()
        # fechar o arquivo

    except FileNotFoundError:
        # caso o arquivo não seja encontrado retorne False
        return False
    else:  # senão retorne True, ou seja, o arquivo existe
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        # 'wt+' -> w: whrite (escrever) t: text (texto) +: criar
        a.close()

    except:  # caso um arquivo de mesmo nome já exista
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso.\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('\033[31mERRO ao ler o arquivo.\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:.<30}{dado[1]:>3} anos')
        # ler o arquivo
    finally:
        a.close()
        # fechar o arquivo após usá-lo


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')

    except:
        print('\033[31mErro na abertura do Arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mErro ao inserir os dados informados.\033[m')
        else:
            print(f'\033[32mNovo registro de {nome} adicionado.\033[m')
            a.close()
