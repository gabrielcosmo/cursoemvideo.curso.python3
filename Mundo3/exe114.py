# exe114 -> Tentar descobrir se um site está diponível ou não
import urllib.request

try:
    site = urllib.request.urlopen('http://globoesporte.globo.com')
except urllib.error.URLError:
    print('\033[31mNão consegui acessar o site.\033[m')
else:
    print('\033[33mConsegui acessar o site com sucesso.')
    # print(site.read()) -> mostra o código html do site
