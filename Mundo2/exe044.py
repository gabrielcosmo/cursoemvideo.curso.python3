# Formas de pagamento de um produto

print('='*10,'Sistema de pagamento','='*10)
pre = float(input('\nPreço do produto: '))
print('-'*50)

#formas de pagamento
print('\nFormas de pagamento: \n\n1- Á vista dinheiro/cheque: 10% de desconto '
      '\n2- Á vista no Cartão: 5% de desconto \n3- Em até 2x no Cartão: preço normal '
      '\n4- 3x ou mais no Cartão: 20% de juros')

forma_pag = int(input('\n'))
print('='*50)

if forma_pag == 1:
    novo_pre = pre - (pre * (10/100))
    print(f'\nCom 10% de desconto o preço do produto a pagar ficará por R${novo_pre:.2f}')

elif forma_pag == 2:
    novo_pre = pre - (pre * (5/100))
    print(f'\nCom 5% de desconto o preço do produto a pagar ficará por R${novo_pre:.2f}')

elif forma_pag == 3:
    print(f'Você optou por parcelar em até 2x no cartão, assim o preço do produto continuará por R${pre}')

elif forma_pag == 4:
    novo_pre = pre + (pre * (20/100))
    parc = int(input('\nQuantas parcelas ? '))
    pre_parc = novo_pre / parc
    print(f'\nO preço do produto terá um acrésimo de 20% de juros no valor total, ficando por R${novo_pre:.2f}')
    print(f'O valor do produto ficará parcelado em {parc} parcelas de R$ {pre_parc}.')

else:
    print('\033[3;31mERROR \nOpção inválida pagamento.\033[m')