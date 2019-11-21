#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Crie um ambiente virtual para instalar os pacotes e não misturar com a estrutura do seu sistema
#   python3 -m venv .venv
#   source .venv/bin/activate
# Tenha instalado os pacotes beautifulsoup e requests:
#   python3 -m pip install requests
#   python3 -m pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup
import sys

# Para solicitar o argumento, no caso o verbete a ser procurado
verbete = sys.argv[1]

url = 'https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/' + verbete


page = requests.get(url)

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Pegar o texto da div verbete bs-component
vocabulos = soup.find(class_='verbete bs-component')

# Pegar o texto de todas as instâncias das tags dentro da div BodyText
vocabulos_items = vocabulos.find_all('acn')
vocabulos_items2 = vocabulos.find_all('div')
vocabulos_items3 = vocabulos.find_all('rn')
vocabulos_items4 = vocabulos.find_all('ra')

# Criar loop para imprimir todos os significados do vocábulo


for vocabulos in vocabulos_items or vocabulos_items2 or vocabulos_items3 or vocabulos_items4:
    print(vocabulos.next_sibling)
