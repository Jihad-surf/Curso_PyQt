import requests

cep = '01153000'

try:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    dic_requisicao = requisicao.json()

    print(dic_requisicao)
    print(dic_requisicao['bairro'])
    print(dic_requisicao['logradouro'])
except:
    print('cep invalido')