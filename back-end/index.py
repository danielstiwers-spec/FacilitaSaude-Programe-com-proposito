
import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

dados = requests.get(url).json()

for estado in dados:
    print(estado["nome"])