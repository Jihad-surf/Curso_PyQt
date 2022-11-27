import requests

cep = ''

link = f'https://viacep.com.br/ws/{cep}/json/'

requisicao = requests.get(link)

dic_requisicao = requisicao.json()

print(dic_requisicao)