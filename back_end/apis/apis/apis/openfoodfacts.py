import requests

def pesquisar(codigo):

    url=f"https://world.openfoodfacts.org/api/v0/product/{codigo}.json"

    return requests.get(url).json()