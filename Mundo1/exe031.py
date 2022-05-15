# Viagem de Ônibus
# Vc paga R$ 0,50/km em viagens até 200 km, e R$ 0,40/km p/ viagens mais longas

dis = int(input('\nDistância percorrida: '))
print('-'*30)

if dis <= 200:
    preco = dis * 0.50
    print(f'Preço a pagar: R$ {preco} \npreço por Km rodado: R$ 0,50.')
    print('-'*30)

if dis > 200:
    preco = dis * 0.45
    print(f'Preço a pagar: R$ {preco} \npreço por Km rodado: R$ 0,45.')
    print('-'*30)