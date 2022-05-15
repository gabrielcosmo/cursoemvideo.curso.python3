# Jogo - Par ou Ímpar
import random
print('\n','='*10,'Par ou Ímpar','='*10,'\n')
jogador = str(input('\n\033[34mJogador: \033[m')).capitalize().strip()     # nome do jogador
personalizar = str(input('\n\033[34mPersonalizar seu nome: [s/n] \033[m')).lower().strip()  # personalizar o nome

dic_cores = {'azul':'\033[34m', 'vermelho':'\033[31m',
             'verde':'\033[32m', 'ciano':'\033[36m'}                 # dicionário p/ cores do nome
lista_rivais = ['\033[31mComputador\033[m','\033[31mA Máquina\033[m',
                '\033[31mO Sistema\033[m','\033[31mXLR-8\033[m']      # lista de nome p/ o computador

vit = 0   # n de vitórias do jogador
tent = 1  # n de tentativas
nome_comp = random.choice(lista_rivais)  # nome do computador
escolha_comp = 0     # escolha do computador par/impar

if personalizar == 's':  # jogador esolhe mudar a cor do nome
    print('-'*20)
    print('''\nVocê pode escolher entre: 
    - azul;
    - vermelho;
    - verde;
    - ciano.''')

    cor_nome = str(input(''))
    while cor_nome not in dic_cores:
        cor_nome = str(input(''))

    jogador = f'{dic_cores[cor_nome]}{jogador}\033[m'    # alterando a cor do nome

    print('-'*20)
    print(f'\n{jogador:^10} vs {nome_comp:^10}')

else:
    print(f'\n{jogador:^10} vs {nome_comp:^10}')

while True:
    comp = random.randint(0, 10)  # lanche do computador
    escolha_jog = str(input('\n\033[34mEscolha o que você é: Par ou Ímapar ? \033[m')).lower().strip()

    while escolha_jog != 'par' and escolha_jog != 'impar':
        escolha_jog = str(input('\n\033[34mEscolha o que você é: Par ou Ímpar ? \033[m')).lower().strip()

    lanche_jog = int(input('\n\033[34mQue NÚMERO você joga ? \033[m'))   # lanche do jogador

    if escolha_jog == 'par':
        escolha_comp = 'ímpar'

    if escolha_jog == 'impar' or escolha_jog == 'ímpar':
        escolha_comp = 'par'

    soma = lanche_jog + comp  # sabendo o resultado

    if soma % 2 == 0 and escolha_jog == 'par': # caso de vitória do jogador

        print(f'\n{escolha_jog} {jogador:^10} => {lanche_jog} vs {comp} <= {nome_comp:^10} {escolha_comp}')
        print('\n\033[32mVocê venceu !!\033[m')
        vit += 1

    elif soma % 2 == 1 and escolha_jog == 'impar' or escolha_jog == 'ímpar': # caso de vitória do jogador

        print(f'\n{escolha_jog} {jogador:^10} => {lanche_jog} vs {comp} <= {nome_comp:^10} {escolha_comp}')
        print('\n\033[32mVocê venceu!!\033[m')
        vit += 1

    else: # derrota do jogador

        print(f'\n{escolha_jog} {jogador:^10} => {lanche_jog} vs {comp} <= {nome_comp:^10} {escolha_comp}')
        print('\033[31mVocê perdeu!!!\033[m')
        break

    print('='*30)
    tent += 1   # contando as tentativas
print(f'\nVitórias de {jogador}: {vit} \nTentativas: {tent}')
