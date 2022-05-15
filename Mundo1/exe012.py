# Desconto de um produto

preco = float(input('\nPreço do produto: '))
print('-'*30)
desconto = float(input('Desconto para o preço desse produto: '))

des_por = desconto / 100         #Desconto em porcentagem
des_reais = preco * des_por
des_n_pro = preco - des_reais     #Preço com desconto

print('='*30)
print('Preço final do produto: R$ %s \nDesconto de: R$ %s' % (des_n_pro,des_reais))
