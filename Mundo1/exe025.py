#Encontrando um nome

nome = str(input('\033[32mNome: ')).strip()
proc = str(input('Nome procurado:\033[m ')).strip()  #proc => procurado

nome2 = nome.lower()
proc2 = proc.lower()

res = proc2 in nome2

print(f'\nO nome \033[1;34m{nome}\033[m apresenta o nome \033[1;34m{proc}\033[m ? {res}.')