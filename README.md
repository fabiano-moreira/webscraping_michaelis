Criando um script Python com a função de Scrapy em vocábulos do dicionário Michaelis.
O site será o Michaelis: 
https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro

## Instalação

1 - Faça o clone do projeto:

```bash
https://github.com/fabiano-moreira/webscraping_michaelis.git
```

2 - Crie um ambiente virtual para instalar os pacotes e não misturar com a estrutura do seu sistema


```bash
$ cd webscraping_michaelis
$ python3 -m venv .venv
$ source .venv/bin/activate
```

3 - Instalar as dependências:

```bash
(.venv)$ pip install -r requirements.txt
```

4 - Para utilizar, mande o python executar o script
passando o verbete que deseja pesquisar:

Exemplo: 

```bash
(.venv)$ python3 dicionario_michaelis.py pão
```