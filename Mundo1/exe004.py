#Dissecando  uma Variável

msg = input('Digite qualquer coisa: ')
print('-'*30)

print('O seu tipo primitivo é',type(msg))
print('Ele é alfanumérico ? ',msg.isalnum())
print('É um número ? ',msg.isnumeric())
print('É alfabético ? ',msg.isalpha())
print('É formado por letras maiúsculas ? ',msg.isupper())
print('É formado por letras maiúsculas ? ',msg.islower())
print('Está Capitalizada ? ',msg.istitle())
print('É formado apenas por espaços ? ',msg.isspace())
