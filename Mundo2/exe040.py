# Médias

n1 = float(input('\nPrimeira nota: '))
n2 = float(input('\nSegunda nota: '))
print('')

media = (n1 + n2) / 2

if media < 5:
    print('Sua nota está abaixo de 5. Você foi reprovado. \nMédia: {:.2f}'.format(media))

if 5.0 < media < 6.9:
    print('Sua média está entre 5 e 6.9. Você ficou de recuperação. \nMédia: {:.2f}'.format(media))

if media >= 7:
    print('Parabéns! Você foi aprovado. \nMédia: {:.2f}'.format(media))
