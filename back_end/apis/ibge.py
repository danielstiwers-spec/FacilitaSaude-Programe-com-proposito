import requests

def listar_estados():

    url="https://servicodados.ibge.gov.br/api/v1/localidades/estados"

    resposta=requests.get(url)

    return resposta.json()