#Enontrando uma letra em uma frase

frase = str(input('Digite uma Frase: ')).lower()

print('''\nDigite uma letra e veja: 
- Quantas vezes ela aparece;
- Em que posição ela aparece pela priemira vaz;
- Em que posição ela aparece pela última vez.''')

letra = str(input('\n')).lower()

q_letra = frase.count(letra)
p_vez = frase.find(letra)
u_vez = frase.rfind(letra)

print(f'''A letra {letra} aparece {q_letra} vezes 
\nA primeira letra {letra} aparece na posição {p_vez + 1} 
\nA última letra {letra} aparece na posição {u_vez + 1}''')
