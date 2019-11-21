
# Tenha instalado os pacotes beautifulsoup e requests:
#   pip install beautifulsoup4
#   pip install requests
import requests
from bs4 import BeautifulSoup

req = requests.get('https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

